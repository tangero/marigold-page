---
slug: "mep"
url: "/mobilnisite/slovnik/mep/"
type: "slovnik"
title: "MEP – Multi-access Edge Platform"
date: 2026-01-01
abbr: "MEP"
fullName: "Multi-access Edge Platform"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mep/"
summary: "Multi-access Edge Platform (MEP) je standardizované výkonové prostředí na okraji sítě, definované organizací ETSI. V rámci 3GPP umožňuje hostování a správu aplikací v blízkosti uživatele. Poskytuje kl"
---

MEP je standardizované výkonové prostředí na okraji sítě, které umožňuje hostování a správu aplikací v blízkosti uživatele za účelem podpory služeb s nízkou latencí.

## Popis

Multi-access Edge Platform (MEP) je standardizovaný rámec, původně definovaný skupinou [ETSI](/mobilnisite/slovnik/etsi/) ISG [MEC](/mobilnisite/slovnik/mec/) a integrovaný do architektury 3GPP, který poskytuje cloudovou výpočetní platformu a servisní prostředí na okraji mobilní sítě. Je nasazován uvnitř sítě operátora, typicky na místech jako centrální ústředny, agregační body nebo přímo na lokalitě základnové stanice (gNB), aby hostoval aplikace a služby v těsné blízkosti koncových uživatelů. Primární funkcí MEP je zpřístupňovat okrajové služby a schopnosti autorizovaným aplikacím, které jsou zabaleny jako Virtual Network Functions (VNFs) nebo Container Network Functions (CNFs). Spravuje životní cyklus těchto aplikací, včetně jejich vytváření instancí, ukončování a přesunu.

Architektonicky se MEP skládá z několika klíčových komponent. MEP Platform Manager (MEPM) je zodpovědný za celkovou správu a orchestraci platformy MEP a aplikací na ní běžících. MEP Orchestrator ([MEO](/mobilnisite/slovnik/meo/)) se stará o onboarding aplikačních balíčků, spravuje aplikační pravidla a požadavky a spouští vytváření a ukončování instancí aplikací. Uvnitř samotného MEP běží MEP Host na virtualizační infrastruktuře (např. hypervizor nebo container runtime) a hostuje MEP Platformu. Tato platforma zahrnuje MEP Service Registry, která katalogizuje dostupné okrajové služby, a funkci Traffic Rules Control, která může na základě politik směrovat uživatelskou rovinu provozu na příslušnou hostovanou aplikaci. Zásadně důležitá je integrace MEP s 5G Core Network od 3GPP, konkrétně s Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) a Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)), pro přístup k síťovému a uživatelskému kontextu (jako je lokalita a QoS) a pro ovlivňování směrování provozu přes User Plane Function ([UPF](/mobilnisite/slovnik/upf/)).

Jak to funguje, zahrnuje koordinovaný tok. Když je identifikován požadavek na službu vyžadující okrajové zpracování (např. [AR](/mobilnisite/slovnik/ar/) sezení), může 5G core síť prostřednictvím NEF nebo PCF komunikovat s MEP Orchestrátorem. Orchestrátor vybere vhodného MEP Hosta na základě uživatelovy polohy a potřeb aplikace, vytvoří instanci aplikace a nakonfiguruje potřebná pravidla pro provoz. Tato pravidla jsou pak vynucována UPF, která přesměruje příslušný provoz uživatelské roviny na aplikaci hostovanou na MEP místo jeho odeslání do vzdáleného datového centra. Aplikace zpracovává data s minimální latencí, využívajíc místní kontext zpřístupněný platformou MEP, a výsledek vrací přímo uživateli nebo do core sítě. Tato interakce v uzavřené smyčce mezi 5G jádrem a MEP je zásadní pro poskytování služeb ultra-spolehlivé komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a vylepšeného mobilního širokopásmového přístupu (eMBB).

## K čemu slouží

Multi-access Edge Platform byla vytvořena, aby řešila základní omezení centralizovaného cloud computingu pro aplikace citlivé na latenci a využívající kontext. Jak se mobilní služby vyvíjely směrem k rozšířené realitě, autonomnímu řízení, průmyslovému IoT a analýze videa v reálném čase, zpoždění způsobené cestou do vzdálených hyperscale datových center se stalo kritickým úzkým hrdlem. Účelem MEP je přinést cloudové schopnosti – výpočetní výkon, úložiště a síťování – až na samý okraj přístupové sítě, čímž se drasticky sníží latence, ušetří se přenosová kapacita backhaulových spojů a umožní se přístup k síťovému a uživatelskému kontextu v reálném čase.

Řeší problém servisních sil a vazby na konkrétního dodavatele (vendor lock-in) na okraji sítě. Před standardizací byla řešení pro edge computing často proprietární, což ztěžovalo vývojářům aplikací napsat kód jednou a nasadit jej napříč různými sítěmi operátorů. MEP jako standardizovaná platforma poskytuje společnou sadu API a konzistentní prostředí. To umožňuje vývojářům třetích stran vytvářet aplikace, které mohou běžet na jakémkoli kompatibilním nasazení MEP, a podporuje tak ekosystém okrajových aplikací. Také řeší výzvu efektivního využití zdrojů na okraji sítě tím, že poskytuje spravovanou, orchestrační platformu, která může dynamicky škálovat aplikace na základě poptávky.

Historicky koncept vznikl z Mobile Edge Computing (MEC) v ETSI, který byl později přejmenován na Multi-access Edge Computing, aby zahrnul pevné a další přístupové technologie. Integrace MEP do 3GPP, zejména od Release 15 dále, byla motivována principem návrhu 5G, kterým je nativní podpora edge computingu. Řeší omezení předchozích přístupů, kde bylo okrajové zpracování dodatečnou úvahou vyžadující komplexní a nestandardní integrace. Definováním jasných referenčních bodů mezi 5G jádrem (zejména NEF, PCF, UPF) a MEP umožňuje 3GPP automatizované, politikami řízené směrování provozu a zpřístupňování služeb, což je nezbytné pro naplnění plného potenciálu vertikálních služeb 5G.

## Klíčové vlastnosti

- Standardizované výkonové prostředí pro hostování VNF/CNF na okraji sítě
- Integruje se s 5GC přes NEF a PCF pro orchestraci služeb využívajících kontext
- Zahrnuje MEP Platform Manager (MEPM) a MEP Orchestrator (MEO) pro správu životního cyklu
- Poskytuje schopnosti směrování provozu pro přesměrování toků uživatelské roviny na lokální aplikace přes UPF
- Zpřístupňuje okrajové služby (jako lokalita, správa šířky pásma) aplikacím prostřednictvím standardizovaných API
- Podporuje mobilitu aplikací a přesun jejich stavu pro bezproblémový uživatelský zážitek

## Související pojmy

- [MEC – Multi-Access Edge Computing](/mobilnisite/slovnik/mec/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)

## Definující specifikace

- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.806** (Rel-7) — Voice Call Continuity between CS and IMS
- **TR 23.958** (Rel-19) — EDGEAPP alignment with ETSI MEC and GSMA OP
- **TS 32.818** (Rel-8) — SA5 MTOSI XML Harmonization Study

---

📖 **Anglický originál a plná specifikace:** [MEP na 3GPP Explorer](https://3gpp-explorer.com/glossary/mep/)
