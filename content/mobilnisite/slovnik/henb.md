---
slug: "henb"
url: "/mobilnisite/slovnik/henb/"
type: "slovnik"
title: "HENB – Home Enhanced Node B"
date: 2025-01-01
abbr: "HENB"
fullName: "Home Enhanced Node B"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/henb/"
summary: "Home Enhanced Node B (HeNB) je femtobuňková stanice LTE umístěná u zákazníka, která poskytuje lokalizované pokrytí mobilním signálem a připojuje se k jádru sítě operátora přes domácí širokopásmové při"
---

HENB je femtobuňková stanice LTE (femtocell) umístěná u zákazníka, která poskytuje lokalizované pokrytí mobilním signálem uvnitř budov připojením k jádru sítě operátora přes domácí širokopásmové připojení.

## Popis

Home Enhanced Node B (HeNB) je nízkovýkonová, uživatelem nasazená základnová stanice LTE určená pro domácí nebo kancelářské prostředí. Jedná se o standardizovaný 3GPP termín pro femtobuňku LTE. Funkčně zahrnuje schopnosti plnohodnotné stanice eNodeB (základnové stanice LTE), ale je optimalizovaná z hlediska nákladů, velikosti a zjednodušené obsluhy. HeNB poskytuje rádiové pokrytí pro LTE uživatelská zařízení (UE) v omezené oblasti, typicky v domácnosti, a vytváří malou buňku (small cell), která je integrována do makro sítě mobilního operátora. K jádru sítě operátora (Evolved Packet Core – EPC) se nepřipojuje přes vyhrazenou přenosovou síť (backhaul), ale prostřednictvím stávajícího širokopásmového internetového připojení uživatele (např. [DSL](/mobilnisite/slovnik/dsl/), kabel, optické vlákno) za použití zabezpečeného tunelu [IPsec](/mobilnisite/slovnik/ipsec/).

Z architektonického hlediska se HeNB skládá z LTE rádiové jednotky, základnové pásmo (baseband) a nezbytné klientské funkce bezpečnostní brány (SeGW). S EPC komunikuje přes bránu HeNB Gateway (HeNB GW), což je volitelný síťový prvek zavedený pro agregaci provozu z velkého počtu HeNB, čímž se snižuje signalizační zátěž na uzlech jádra sítě, jako je [MME](/mobilnisite/slovnik/mme/) a S-GW/[P-GW](/mobilnisite/slovnik/p-gw/). HeNB GW funguje jako koncentrátor, který se vůči MME jeví jako standardní eNodeB a vůči HeNB jako MME. Alternativně se mohou HeNB v menších nasazeních připojovat přímo k MME a S-GW. Mezi klíčové procedury, které HeNB zajišťuje, patří správa rádiových zdrojů (RRM), řízení mobility spojení a celý soubor protokolů LTE vrstvy 1, 2 a 3 pro rozhraní Uu.

Z pohledu sítě přináší subsystém HeNB nové aspekty správy a zabezpečení. Pro vzdálenou konfiguraci, správu softwaru a monitorování poruch se používá HeNB Management System (HeMS). Řízení přístupu je klíčové; HeNB typicky pracuje v jednom ze tří režimů: Closed Access (buňka s uzavřenou skupinou účastníků – [CSG](/mobilnisite/slovnik/csg/), kam mají přístup pouze předem autorizovaní členové), Hybrid Access (prioritizuje členy CSG, ale umožňuje přístup ostatním, pokud to zdroje dovolí) nebo Open Access (funguje jako veřejná buňka). HeNB se k síti autentizuje pomocí certifikátů a vytváří zabezpečený tunel k ochraně všech přenášených dat uživatelské i řídicí roviny přes veřejný internet. To operátorům umožňuje rozšířit pokrytí a kapacitu hluboko do interiérů, kde je signál makro sítě slabý, při zachování kontroly nad kvalitou služeb a zabezpečením.

## K čemu slouží

HeNB byla standardizována v 3GPP Release 8 jako řešení rostoucí výzvy poskytovat kvalitní pokrytí mobilním broadbandem v interiérech, kde vzniká většina datového provozu. Signál makro buněk často výrazně slábne při průchodu budovami, což vede ke špatné síle signálu, nižším datovým rychlostem a přerušeným hovorům pro uživatele uvnitř. Nasazování dalších makro stanic je drahé a naráží na regulační překážky. Koncept HeNB využívá vlastní širokopásmové připojení účastníka k vytvoření cenově efektivního rozšíření sítě instalovaného zákazníkem, čímž řeší problém s pokrytím v interiérech a odlehčuje přenosovou zátěž makro sítě.

Jeho vytvoření bylo také motivováno potřebou standardizované, operátorem řízené alternativy k nelicencovaným bezdrátovým řešením, jako je Wi-Fi. Zatímco přenos na Wi-Fi byl běžný, postrádal plynulou mobilitu, integrovanou autentizaci a konzistentní správu QoS. HeNB poskytuje zážitek na úrovni mobilní sítě s plynulým předáváním spojení k/z makro sítě, integrovanou autentizací účastníka prostřednictvím SIM karty a podporou všech služeb operátora (jako je hlas přes IMS). Standardizace zajistila interoperabilitu mezi HeNB od různých výrobců a jádrem sítě operátora, což umožnilo hromadné nasazení. Definovala také klíčové bezpečnostní architektury pro ochranu sítě operátora před hrozbami pocházejícími z veřejného internetového backhaulu, což byl zásadní problém, který dřívější proprietární řešení femtobuněk musela řešit individuálně.

## Klíčové vlastnosti

- Nízkovýkonová stanice eNodeB LTE pro nasazení u koncového zákazníka
- Připojuje se k EPC operátora přes domácí IP broadband a tunel IPsec
- Podporuje režimy Closed, Hybrid a Open Access (CSG)
- Pro škálovatelnost se může připojovat přes volitelnou bránu HeNB Gateway
- Obsahuje integrovaného klienta bezpečnostní brány pro zabezpečený backhaul
- Vzdáleně spravována systémem HeNB Management System (HeMS) pro konfiguraci a aktualizace

## Související pojmy

- [CSG – Closed Subscriber Group](/mobilnisite/slovnik/csg/)

## Definující specifikace

- **TS 23.830** (Rel-9) — Home NodeB/HeNB Architecture and CSG Study
- **TR 25.967** (Rel-19) — Home NodeB RF Requirements Technical Report

---

📖 **Anglický originál a plná specifikace:** [HENB na 3GPP Explorer](https://3gpp-explorer.com/glossary/henb/)
