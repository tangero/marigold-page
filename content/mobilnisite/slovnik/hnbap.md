---
slug: "hnbap"
url: "/mobilnisite/slovnik/hnbap/"
type: "slovnik"
title: "HNBAP – Home Node B Application Part"
date: 2025-01-01
abbr: "HNBAP"
fullName: "Home Node B Application Part"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hnbap/"
summary: "HNBAP je řídicí protokol používaný mezi Home Node B (HNB) a bránou HNB (HNB-GW) v 3GPP femtobuňkových sítích. Spravuje registraci, konfiguraci a řízení HNB, což umožňuje bezpečný a efektivní provoz ma"
---

HNBAP je řídicí protokol mezi Home Node B a její bránou (Gateway), který spravuje registraci, konfiguraci a řízení femtobuňky pro její bezpečnou integraci do mobilní páteřní sítě.

## Popis

Home Node B Application Part (HNBAP) je klíčový řídicí protokol definovaný ve specifikaci rozhraní Iuh 3GPP. Působí mezi Home Node B ([HNB](/mobilnisite/slovnik/hnb/)), což je femtobuňka pro koncové uživatele, a bránou HNB ([HNB-GW](/mobilnisite/slovnik/hnb-gw/)), která agreguje provoz z více HNB a připojuje je k páteřní síti. HNBAP je zodpovědný za řídicí a správní funkce nezbytné pro uvedení HNB do provozu a udržení jejího chodu. Je analogický k protokolu Node B Application Part ([NBAP](/mobilnisite/slovnik/nbap/)) používanému v makrobuněčných sítích, ale je přizpůsoben specifickým požadavkům architektury femtobuněk, včetně zabezpečení a škálovatelnosti pro potenciálně miliony nasazených jednotek.

Protokol funguje nad asociacemi Stream Control Transmission Protocol (SCTP), což zajišťuje spolehlivé doručování zpráv. Jeho hlavní funkce se dělí do dvou hlavních kategorií: Registrace HNB a Konfigurace HNB. Registrační procedury umožňují HNB autentizovat se u HNB-GW a páteřní sítě, ověřit její identitu, polohu a autorizovanou oblast služeb. Tento proces zahrnuje vzájemnou autentizaci a vytvoření bezpečnostních kontextů. Konfigurační procedury slouží ke správě provozních parametrů HNB, jako jsou nastavení rádiové frekvence (RF), seznamy sousedních buněk a systémové informační bloky (SIB). HNB-GW používá HNBAP k zasílání konfiguračních aktualizací a řízení správy rádiových zdrojů HNB za účelem minimalizace interference s makro sítí.

Klíčové architektonické komponenty spojené s HNBAP zahrnují samotnou HNB, HNB-GW a Bezpečnostní bránu (SeGW). SeGW nejprve vytvoří s HNB tunel [IPsec](/mobilnisite/slovnik/ipsec/) pro zabezpečený přenos, a teprve poté probíhá signalizace HNBAP. Zprávy HNBAP jsou následně přenášeny uvnitř tohoto zabezpečeného tunelu. Protokol definuje řadu elementárních procedur ([EP](/mobilnisite/slovnik/ep/)) pro konkrétní úkoly, jako je HNB Register, HNB De-register, HNB Configuration Update a Error Indication. Zpracovává také procedury registrace UE pro uživatelská zařízení připojující se přes HNB. Role HNBAP je zásadní; umožňuje subsystému HNB, aby se z pohledu páteřní sítě jevil jako standardní Radio Network Controller (RNC), což umožňuje znovupoužití stávajících rozhraní a funkcí páteřní sítě pro provoz femtobuněk.

## K čemu slouží

HNBAP byl vytvořen, aby řešil specifické problémy řízení a správy spojené s hromadným nasazením femtobuněk (Home Node B) ve 3GPP Release 8. Před femtobuňkami byly mobilní sítě budovány výhradně na infrastruktuře makrobuněk nasazených operátorem. Zavedení malých buněk instalovaných zákazníky vyžadovalo novou architekturu, která by byla škálovatelná na miliony jednotek, zajistila robustní zabezpečení proti vniknutí do sítě a uměla spravovat rádiové zdroje, aby nedocházelo k interferenci se stávající makro sítí. Stávající řídicí protokoly pro makrobuňky, jako je [NBAP](/mobilnisite/slovnik/nbap/), nebyly pro toto nezabezpečené prostředí rezidenčního IP přenosu navrženy.

Hlavním problémem, který HNBAP řeší, je bezpečná a škálovatelná integrace nedůvěryhodných přístupových bodů ve vlastnictví zákazníků do důvěryhodné sítě operátora. Poskytuje standardizovanou signalizaci nezbytnou pro to, aby se [HNB](/mobilnisite/slovnik/hnb/) mohla inicializovat, autentizovat svou polohu a identitu, přijímat provozní konfiguraci ze sítě a spravovat životní cyklus připojených UE. To umožňuje operátorům nabízet lepší vnitřní pokrytí a kapacitu pomocí zařízení umístěných u zákazníka, aniž by byla ohrožena bezpečnost nebo stabilita sítě. Motivací při návrhu protokolu bylo umožnit zákazníkům instalaci typu plug-and-play, operátorům centralizované řízení a efektivní využití licencovaného spektra prostřednictvím správy výkonu a frekvencí femtobuněk pomocí konfigurace řízené sítí.

## Klíčové vlastnosti

- Spravuje registraci a autentizaci HNB u páteřní sítě
- Přenáší konfigurační data (RF parametry, seznamy sousedních buněk) z HNB-GW na HNB
- Řídí navázání a uvolnění signalizačních spojení pro UE
- Podporuje procedury hlášení chyb a správy poruch
- Funguje nad SCTP pro spolehlivý přenos uvnitř zabezpečeného tunelu IPsec
- Definuje procedury pro odregistrování HNB a aktualizace konfigurace

## Související pojmy

- [HNB – Home Node B](/mobilnisite/slovnik/hnb/)
- [HNB-GW – Home Node B Gateway](/mobilnisite/slovnik/hnb-gw/)
- [NBAP – Node B Application Protocol](/mobilnisite/slovnik/nbap/)
- [CSG – Closed Subscriber Group](/mobilnisite/slovnik/csg/)

## Definující specifikace

- **TS 25.469** (Rel-19) — HNBAP Specification for HNB to HNB-GW Interface
- **TS 25.820** (Rel-8) — 3G Home NodeB Study Report
- **TR 25.967** (Rel-19) — Home NodeB RF Requirements Technical Report
- **TS 32.821** (Rel-9) — SON OAM Architecture for Home NodeB

---

📖 **Anglický originál a plná specifikace:** [HNBAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/hnbap/)
