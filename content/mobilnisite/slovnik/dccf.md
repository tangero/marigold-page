---
slug: "dccf"
url: "/mobilnisite/slovnik/dccf/"
type: "slovnik"
title: "DCCF – Data Collection and Coordination Function"
date: 2026-01-01
abbr: "DCCF"
fullName: "Data Collection and Coordination Function"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dccf/"
summary: "Funkce sběru a koordinace dat (DCCF) je síťová funkce 5G zavedená ve verzi 17, která spravuje sběr, ukládání a zpřístupňování analytických dat sítě. Působí jako centralizovaný koordinátor mezi produce"
---

DCCF je síťová funkce 5G, která centrálně spravuje sběr, ukládání a na politice založené zpřístupňování analytických dat sítě mezi producenty a konzumenty pro AI/ML a optimalizaci.

## Popis

Funkce sběru a koordinace dat (DCCF) je klíčová řídicí funkce v rámci architektury 5G založené na službách ([SBA](/mobilnisite/slovnik/sba/)), speciálně navržená pro správu životního cyklu sběru dat pro síťovou analytiku a automatizaci. Architektonicky stojí mezi producenty dat – jako jsou síťové funkce ([NF](/mobilnisite/slovnik/nf/)), systémy pro provoz, správu a údržbu ([OAM](/mobilnisite/slovnik/oam/)) a uživatelská zařízení (UE) – a konzumenty dat, jako je funkce pro analýzu síťových dat ([NWDAF](/mobilnisite/slovnik/nwdaf/)) nebo externí aplikační funkce ([AF](/mobilnisite/slovnik/af/)). DCCF sama neprovádí analytiku, ale zaměřuje se na orchestraci datových toků: přijímá žádosti o sběr dat od konzumentů, překládá je do proveditelných úloh pro producenty, agreguje sebraná data a ukládá je strukturovaným způsobem, často ve spolupráci s funkci pro ukládání dat ([DSF](/mobilnisite/slovnik/dsf/)).

Provozně DCCF funguje prostřednictvím sady standardizovaných rozhraní (např. Ndcf_DataCollectionManagement) definovaných ve specifikacích 3GPP. Když analytický konzument (např. instance NWDAF trénující model pro predikci zatížení) potřebuje konkrétní data, odešle žádost o sběr dat do DCCF. Tato žádost obsahuje parametry, jako je typ dat (např. vzorce mobility UE, metriky zatížení řezu), úroveň podrobnosti sběru, frekvenci a cílové producenty dat. DCCF pak tuto žádost vyhodnotí vůči politikám – které mohou definovat práva přístupu k datům, omezení soukromí nebo ohledy na zatížení sítě – a je-li autorizována, koordinuje s příslušnými producenty zahájení sběru dat. Dokáže zpracovat jak modely sběru dat založené na odběru (kontinuální), tak na principu žádost-odpověď (jednorázové).

Klíčovými součástmi DCCF jsou její mechanismus vynucování politik, logika agregace dat a schopnosti koordinace ukládání. Komponenta vynucování politik zajišťuje, že sběr dat je v souladu s regulačními (např. GDPR), síťovými (např. vyrovnávání zatížení) a obchodními (např. dohody o sdílení dat) politikami. Logika agregace konsoliduje surová data z více zdrojů – které mohou být heterogenní ve formátu nebo časování – do jednotné, časově označené datové sady vhodné pro analytiku. Koordinace ukládání zahrnuje správu životního cyklu sebraných dat v DSF, včetně doby uchovávání, indexace a zpřístupnění konzumentům. DCCF také poskytuje konzumentům oznámení o stavu úloh sběru dat (např. dokončení, selhání).

V širším síťovém ekosystému hraje DCCF zásadní roli při umožnění daty řízené automatizace a operací se zpětnou vazbou v 5G a budoucích sítích. Oddělením sběru dat od analytiky umožňuje analytickým funkcím být odlehčenější a soustředit se na provádění modelů, zatímco DCCF zvládá náročnou práci se získáváním a správou dat. Toto oddělení odpovědností zlepšuje škálovatelnost, protože jediná DCCF může obsluhovat více instancí NWDAF nebo externích AF. Dále DCCF usnadňuje síťové krájení tím, že umožňuje politiky sběru dat specifické pro jednotlivé řezy – zajišťuje, že data z jednoho řezu nejsou neúmyslně zpřístupněna analytickým procesům jiného řezu. Její integrace s 5G SBA zajišťuje, že může využívat stávající mechanismy registrace služeb, jejich zjišťování a zabezpečení (např. prostřednictvím [NRF](/mobilnisite/slovnik/nrf/) a [SCP](/mobilnisite/slovnik/scp/)).

## K čemu slouží

DCCF byla vytvořena, aby řešila rostoucí složitost a objem dat potřebných pro AI/ML řízenou síťovou automatizaci v 5G. Před verzí 17 byl sběr dat pro analytiku do značné míry ad-hoc: každá analytická funkce (jako NWDAF) musela přímo komunikovat s producenty dat, což vedlo k redundantním datovým žádostem, nekonzistentním datovým formátům a neefektivnímu využití síťových zdrojů. Například dvě instance NWDAF predikující zahlcení a optimalizující předávání hovorů mohly samostatně žádat o podobná data o mobilitě UE od stejné AMF, čímž se signalizační režie zdvojnásobila. Také neexistoval žádný centralizovaný mechanismus pro vynucování politik přístupu k datům nebo ochrany soukromí napříč více analytickými konzumenty, což zvyšovalo riziko nedodržení předpisů.

Historicky se síťový management spoléhal na statické OAM systémy s periodickým reportováním, ale dynamická povaha 5G – s funkcemi jako síťové krájení, edge computing a ultra-spolehlivá nízkolatenční komunikace (URLLC) – vyžaduje data v reálném čase a s vysokou podrobností pro proaktivní optimalizaci. Omezení předchozích přístupů se stala zjevnými, když operátoři nasazovali NWDAF pro případy užití, jako je vyrovnávání zatížení a detekce anomálií; bez koordinátoru síť čelila problémům se škálovatelností, zejména s rozšiřováním zařízení internetu věcí (IoT) a síťových řezů generujících terabajty dat denně.

DCCF tyto problémy řeší zavedením standardizovaného, centralizovaného rámce pro sběr dat. Snižuje signalizační režii agregací žádostí a efektivním distribucí dat, zajišťuje dodržování politik prostřednictvím jednotného bodu vynucování a poskytuje konzistentní datový model (sladěný se specifikacemi 3GPP), který zjednodušuje vývoj analytiky. Její vytvoření bylo motivováno posunem průmyslu směrem k síťování založenému na záměrech a autonomním operacím, kde jsou spolehlivá a kvalitní data palivem pro AI/ML modely. Oddělením sběru dat od analytiky DCCF připravuje síť na budoucí aplikace, jako jsou digitální dvojčata, imerzivní služby a výzkum 6G, které budou vyžadovat ještě rozmanitější a objemnější datové sady.

## Klíčové vlastnosti

- Centralizovaná koordinace žádostí o sběr dat od více analytických konzumentů
- Vynucování na základě politik pro přístup k datům, ochranu soukromí a správu zatížení sítě
- Podpora jak modelů sběru dat založených na odběru, tak na principu žádost-odpověď
- Agregace a koordinace ukládání heterogenních dat z NF, OAM a UE
- Standardizovaná rozhraní (např. Ndcf) pro integraci s architekturou 5G založenou na službách
- Škálovatelný návrh pro zvládání vysokokapacitních datových toků napříč síťovými řezy a edge lokalitami

## Související pojmy

- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)
- [DSF – Domain Selection Function](/mobilnisite/slovnik/dsf/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 29.503** (Rel-19) — UDM Service Based Interface Stage 3
- **TS 29.508** (Rel-19) — 5G Session Management Event Exposure Service
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.517** (Rel-19) — 5G AF Event Exposure Service Stage 3
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 29.520** (Rel-19) — 5G Network Data Analytics Services Stage 3
- **TS 29.536** (Rel-19) — NSACF Service Based Interface Protocol
- **TS 29.552** (Rel-19) — 5G Network Data Analytics Signalling Flows
- **TS 29.564** (Rel-19) — Nupf Service Based Interface Protocol
- **TS 29.574** (Rel-19) — 5G Data Collection Coordination Services Stage 3
- **TS 29.575** (Rel-19) — 5G Analytics Data Repository Services Stage 3
- **TS 29.576** (Rel-19) — 5G Messaging Framework Adaptor Services Stage 3
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [DCCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/dccf/)
