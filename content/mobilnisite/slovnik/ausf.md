---
slug: "ausf"
url: "/mobilnisite/slovnik/ausf/"
type: "slovnik"
title: "AUSF – Authentication Server Function"
date: 2026-01-01
abbr: "AUSF"
fullName: "Authentication Server Function"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ausf/"
summary: "AUSF je funkce jádra sítě v 5G, která provádí primární autentizaci a dohodu klíčů (AKA) pro uživatelské zařízení (UE). Je klíčovou součástí bezpečnostní architektury 3GPP a zajišťuje bezpečný přístup"
---

AUSF je funkce jádra sítě 5G, která provádí primární autentizaci a dohodu klíčů za účelem ověření identity účastníka a vytvoření bezpečných relacích klíčů pro přístup ke službám.

## Popis

Authentication Server Function (AUSF) je klíčová komponenta v bezpečnostní architektuře jádra sítě 5G (5GC), konkrétně součást frameworku Security Anchor Function (SEAF). Nachází se v domácí veřejné pozemní mobilní síti ([HPLMN](/mobilnisite/slovnik/hplmn/)) a je zodpovědná za provedení primární autentizační procedury s uživatelským zařízením (UE). AUSF komunikuje s funkcí Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) za účelem získání autentizačních přihlašovacích údajů a dat o předplatném a s funkcí Security Anchor Function (SEAF), která je obvykle umístěna společně s funkcí Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v servisní síti, aby předala autentizační vektory a výsledky. AUSF sama dlouhodobé přihlašovací údaje neukládá; místo toho funguje jako přepojovací a zpracovatelský uzel, který orchestruje metody založené na 5G Authentication and Key Agreement (5G-AKA) nebo Extensible Authentication Protocol ([EAP](/mobilnisite/slovnik/eap/)) definované 3GPP.

Během autentizační procedury, když se UE pokouší registrovat v síti, SEAF/AMF požádá o autentizaci od AUSF. AUSF následně interaguje s UDM/[ARPF](/mobilnisite/slovnik/arpf/) (Authentication Credential Repository and Processing Function), aby získala autentizační vektor. Tento vektor obsahuje náhodnou výzvu (RAND), očekávanou odpověď (XRES*), autentizační token sítě ([AUTN](/mobilnisite/slovnik/autn/)) a klíčový materiál: kotvící klíč (K_AUSF). AUSF přepošle RAND a AUTN k UE prostřednictvím SEAF. UE vypočte odpověď (RES*) pomocí svého uloženého klíče účastníka a odešle ji zpět. AUSF porovná přijaté RES* s XRES* od UDM. Po úspěšném ověření AUSF vygeneruje primární relací klíče: K_SEAF (pro SEAF) a kotvící klíč K_AUSF, který slouží jako kořen pro odvození dalších klíčů pro následné bezpečnostní kontexty.

Role AUSF je klíčová pro vytvoření řetězce důvěry. Klíč K_AUSF, který vygeneruje nebo přijme, se stane kořenovým klíčem pro celý bezpečnostní kontext dané registrační relace. Z K_AUSF se následně odvozují další klíče pro zabezpečení přístupové sítě (K_AMF), integritu a důvěrnost signalizace [NAS](/mobilnisite/slovnik/nas/) a integritu uživatelské roviny (pokud je povolena). Tato hierarchická derivace klíčů zajišťuje jejich oddělení a omezuje dopad případného kompromitování klíče. Dále AUSF podporuje procedury opětovné autentizace a obnovy klíčů. Její architektura je navržena jako bezstavová funkce, přičemž trvalý stav uchovává UDM, což napomáhá škálovatelnosti a spolehlivosti v cloud-nativních nasazeních.

Klíčovým architektonickým pokrokem v 5G je oddělení autentizačního serveru (AUSF) od úložiště dat o předplatném (UDM). Toto zvyšuje bezpečnost omezením vystavení citlivých dlouhodobých klíčů a umožňuje nezávislé škálování autentizační zátěže. AUSF také hraje roli při podpoře autentizace pro nepřístupy 3GPP (např. Wi-Fi) prostřednictvím Non-3GPP InterWorking Function ([N3IWF](/mobilnisite/slovnik/n3iwf/)) a je nedílnou součástí bezpečnostního frameworku pro síťové segmenty (network slicing), čímž zajišťuje, že autentizační politiky mohou být specifické pro segment. Pro tyto interakce jsou definována její rozhraní, jako je Nausf (service-based interface) a N13 (referenční bodové rozhraní k UDM).

## K čemu slouží

AUSF byla zavedena ve specifikaci 3GPP Release 15 jako základní část nové servisně orientované architektury (SBA) jádra 5G s cílem řešit vyvíjející se bezpečnostní požadavky, které předchozí generace neuspokojivě pokrývaly. V 4G EPS byla autentizační funkce integrována v rámci Home Subscriber Server (HSS) a Mobility Management Entity (MME) přes rozhraní S6a. Tento monolitický přístup představoval omezení ve škálovatelnosti, flexibilitě a granularitě zabezpečení. Návrhové principy 5G vyžadovaly více rozčleněnou, cloud-nativní a servisně orientovanou architekturu pro podporu různorodých případů užití, jako je hromadný IoT, ultra-spolehlivá komunikace s nízkou latencí a síťové segmenty (network slicing).

Primárním účelem AUSF je poskytnout vyhrazenou, škálovatelnou funkci pro provádění robustní primární autentizace. Oddělením autentizace od správy dat předplatného (kterou zajišťuje UDM) systém dosahuje silnější bezpečnostní pozice díky principu nejnižších oprávnění. Žádná síťová funkce nedrží všechna citlivá data (dlouhodobý klíč i profil předplatného), čímž se redukuje útočná plocha. Toto oddělení také umožňuje optimalizovat AUSF pro vysoký objem autentizačních transakcí, což je klíčové pro scénáře IoT s miliony zařízení. Dále AUSF umožňuje podporu nových, flexibilnějších autentizačních metod, jako je EAP-5G, která umožňuje integraci s přihlašovacími údaji mimo 3GPP a autentizačními servery třetích stran, což je nezbytné pro podnikové a průmyslové aplikace.

Dalším klíčovým motivem bylo vytvoření trvalé bezpečnostní kotvy (security anchor) v domácí síti. Klíč K_AUSF vygenerovaný během autentizace zůstává stabilní v domácí síti, i když se UE pohybuje mezi různými servisními sítěmi nebo typy přístupu (3GPP, non-3GPP). Tento model 'home control' zvyšuje bezpečnost tím, že zajišťuje, že domácí operátor vždy ověří identitu účastníka a kontroluje kořen hierarchie klíčů. Řeší problém přenosu klíčového kontextu přes síťové hranice, který existoval v předchozích systémech, a poskytuje čistší a bezpečnější framework zabezpečení mobility. AUSF tedy není jen evolučním krokem, ale zásadním přepracováním bezpečnosti pro 5G, které umožňuje důvěru, škálovatelnost a flexibilitu služeb.

## Klíčové vlastnosti

- Provádí primární autentizační procedury založené na 5G-AKA a EAP
- Generuje a spravuje kotvící klíč (K_AUSF) pro hierarchii bezpečnostního kontextu
- Komunikuje s UDM/ARPF za účelem získání autentizačních vektorů a dat o předplatném
- Podporuje autentizaci pro přístupové sítě 3GPP i non-3GPP
- Umožňuje směrování autentizace do domácí sítě (home-routed), čímž udržuje bezpečnostní kotvu (security anchor) v HPLMN
- Usnadňuje opětovnou autentizaci a obnovu klíčů pro zachování bezpečnosti probíhající relace

## Související pojmy

- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 26.891** (Rel-16) — Media Distribution Services in 5G System
- **TS 29.503** (Rel-19) — UDM Service Based Interface Stage 3
- **TS 29.509** (Rel-19) — AUSF Service Based Interface Protocol
- **TS 29.535** (Rel-19) — 5G AKMA Anchor Services Stage 3 Protocol
- **TS 32.255** (Rel-20) — Telecom Management; Charging for 5G Data Connectivity
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.514** (Rel-20) — 5G Security Assurance for UDM
- **TS 33.535** (Rel-19) — 5G AKMA: Authentication and Key Management for Apps
- **TS 33.545** (Rel-19) — Security for NR Femto Subsystem
- **TS 33.701** (Rel-19) — Study on mitigations against bidding down attacks
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [AUSF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ausf/)
