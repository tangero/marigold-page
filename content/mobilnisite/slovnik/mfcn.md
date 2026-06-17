---
slug: "mfcn"
url: "/mobilnisite/slovnik/mfcn/"
type: "slovnik"
title: "MFCN – Mobile / Fixed Communication Networks"
date: 2025-01-01
abbr: "MFCN"
fullName: "Mobile / Fixed Communication Networks"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mfcn/"
summary: "3GPP termín zahrnující kombinovanou nebo konvergovanou síťovou infrastrukturu podporující jak mobilní, tak pevný bezdrátový přístup. Odkazuje na architektonické scénáře a scénáře nasazení, kde společn"
---

MFCN je 3GPP termín pro konvergovanou síťovou infrastrukturu, kde společný core a rádiová přístupová síť (RAN) poskytují služby jak tradičním mobilním zařízením, tak pevným bezdrátovým koncovým zařízením (CPE).

## Popis

Mobile / Fixed Communication Networks (MFCN) je široký termín používaný ve specifikacích 3GPP k popisu nasazení sítí a architektur, které podporují jak služby mobilní komunikace (např. smartphony, tablety), tak služby pevného bezdrátového přístupu ([FWA](/mobilnisite/slovnik/fwa/)). V nasazení MFCN je stejná infrastruktura rádiové přístupové sítě (RAN), jako je 5G NR základnová stanice (gNB), a stejný 5G Core síťový core využívána k obsluze uživatelských zařízení (UE) s vysokou mobilitou i pevných koncových zařízení ([CPE](/mobilnisite/slovnik/cpe/)), která jsou stacionární nebo nominálně přenosná. CPE funguje jako rezidenční nebo firemní brána, poskytující pevné širokopásmové připojení koncovým uživatelským zařízením prostřednictvím Wi-Fi nebo Ethernetu.

Z architektonického hlediska MFCN zahrnuje specifické úvahy jak v RAN, tak v core síti. V RAN to zahrnuje podporu funkcí specifických pro pevný bezdrátový přístup, jako je vylepšené beamforming pro stacionární CPE, modulační schémata vyšších řádů využívající stabilní podmínky kanálu a potenciálně odlišné plánovací algoritmy optimalizované pro stacionární uživatele s konzistentními charakteristikami provozu. gNB musí zvládat mix typů UE a rozlišovat mezi nimi při přidělování zdrojů a správě mobility. V core síti [AMF](/mobilnisite/slovnik/amf/) a [SMF](/mobilnisite/slovnik/smf/) obsluhují relace jak pro mobilní UE, tak pro pevná CPE. Pro FWA však mohou být postupy mobility, jako je předávání hovoru (handover), zjednodušeny nebo nejsou potřeba, a správa relací může upřednostňovat charakteristiky vysoké propustnosti a nízké latence typické pro pevný broadband.

Klíčové technické aspekty pokryté ve specifikacích týkajících se MFCN zahrnují požadavky na koexistenci, sdílení spektra a požadavky na výkon. Specifikace definují požadavky na rádiové kmitočty (RF) pro základnové stanice a uživatelská zařízení pracující v pásmech MFCN, aby zajišťovaly, že zavedení služeb FWA nezhorší výkon pro mobilní uživatele. Dále pokrývají scénáře nasazení, například zda mobilní a pevné služby fungují na stejném kanálu (ko-kanálově) nebo na oddělených kanálech (na sousedním kanále). Metodologie testování výkonu pro propustnost, latenci a spolehlivost jsou specifikovány odděleně pro mobilní a pevné případy užití, aby bylo zajištěno odpovídající plnění potřeb obou skupin. Koncept je klíčový pro trend konvergence, který umožňuje operátorům využít jedinou jednotnou síťovou infrastrukturu k efektivnímu pokrytí více tržních segmentů.

## K čemu slouží

Koncept MFCN byl formalizován, aby reagoval na rostoucí trh s pevným bezdrátovým přístupem ([FWA](/mobilnisite/slovnik/fwa/)) jako primárním širokopásmovým řešením, zejména využívajícím technologii 5G. Poskytuje standardizovaný rámec v rámci 3GPP, který operátorům umožňuje nasadit jedinou síť schopnou obsloužit jak tradiční mobilní účastníky, tak pevné broadbandové zákazníky, čímž maximalizuje návratnost investic do infrastruktury (ROI) a provozní efektivitu. Před tímto explicitním zpracováním nasazení FWA často používala modifikované mobilní sítě bez standardizovaných výkonnostních měřítek nebo pravidel koexistence.

Vytvoření specifikací MFCN řeší několik problémů. Za prvé zajišťuje spektrální efektivitu a harmonickou koexistenci mezi mobilními a pevnými službami sdílejícími stejné spektrum, definováním technických požadavků k zabránění interference. Za druhé poskytuje jasné výkonnostní cíle (např. špičkové přenosové rychlosti, latenci) pro FWA, což umožňuje výrobcům a operátorům navrhovat a certifikovat zařízení. Za třetí usnadňuje konvergenci správy sítě a operací pro oba typy služeb. Historický kontext zahrnuje vývoj od využití 4G LTE pro raná FWA až po vylepšené schopnosti 5G NR (mmWave, massive [MIMO](/mobilnisite/slovnik/mimo/)), které činí výkonné FWA komerčně životaschopnou alternativou k vláknu, což si vyžádalo robustní standardy v rámci 3GPP.

## Klíčové vlastnosti

- Podpora obsluhy jak mobilních uživatelských zařízení (UE), tak pevných koncových zařízení (CPE) z jednotné RAN a core sítě
- Definice specifických RF výkonnostních požadavků a požadavků na koexistenci pro základnové stanice a terminály ve sdíleném spektru
- Specifikace scénářů nasazení včetně ko-kanálového (co-channel) a sousedního kanálového (adjacent channel) provozu pro mobilní a pevné služby
- Výkonnostní požadavky a testovací metodologie šité na míru případům užití pevného bezdrátového přístupu (FWA)
- Úvahy pro RAN funkce, jako je beamforming a plánování, optimalizované pro stacionární CPE
- Zpracování relací v core síti s potenciálně odlišnými profily mobility a QoS (Quality of Service) pro pevné oproti mobilním uživatelům

## Definující specifikace

- **TS 32.855** (Rel-14) — Study on OAM Support for Licensed Shared Access
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.858** (Rel-14) — LTE 2.6 GHz SDL Band Technical Report
- **TS 36.895** (Rel-13) — 700 SDL Band for LTE Carrier Aggregation
- **TS 37.104** (Rel-19) — MSR Base Station RF Characteristics
- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TS 37.814** (Rel-12) — L-band Supplemental Downlink for UTRA/E-UTRA
- **TR 37.829** (Rel-18) — Technical Report
- **TR 38.852** (Rel-17) — 1900MHz NR band for European Rail Mobile Radio
- **TR 38.853** (Rel-17) — 900MHz NR Band for European Rail Mobile Radio

---

📖 **Anglický originál a plná specifikace:** [MFCN na 3GPP Explorer](https://3gpp-explorer.com/glossary/mfcn/)
