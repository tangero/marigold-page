---
slug: "dss1"
url: "/mobilnisite/slovnik/dss1/"
type: "slovnik"
title: "DSS1 – Digital Subscriber Signalling System No. One"
date: 2025-01-01
abbr: "DSS1"
fullName: "Digital Subscriber Signalling System No. One"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dss1/"
summary: "Signalizační protokol používaný v digitální síti integrovaných služeb (ISDN) pro řízení hovorů a doplňkové služby mezi účastnickým terminálem a místní ústřednou. V 3GPP je relevantní jako základ pro u"
---

DSS1 je signalizační protokol ISDN pro řízení hovorů mezi účastnickým terminálem a místní ústřednou, který v 3GPP tvoří starší základ pro signalizaci v okruhově přepínaných sítích a pro vývoj směrem k plně IP systémům.

## Popis

Digital Subscriber Signalling System No. 1 (DSS1), standardizovaný [ITU-T](/mobilnisite/slovnik/itu-t/) v sérii Q.930-Q.939 a přijatý 3GPP, je signalizační protokol vrstvy 3 pro kanál D v [ISDN](/mobilnisite/slovnik/isdn/). Funguje mezi koncovým zařízením ([TE](/mobilnisite/slovnik/te/)) nebo terminálovým adaptérem ([TA](/mobilnisite/slovnik/ta/)) na straně účastníka a ISDN ústřednou (místní ústřednou - [LE](/mobilnisite/slovnik/le/)) v síti. DSS1 je protokol typu peer-to-peer, který využívá spolehlivou službu spojové vrstvy poskytovanou protokolem [LAPD](/mobilnisite/slovnik/lapd/) (Link Access Procedure on the D-channel, Q.921) na uživatelsko-síťovém rozhraní ([UNI](/mobilnisite/slovnik/uni/)).

Z architektonického hlediska je DSS1 součástí řídicí roviny pro okruhově přepínané služby. Jeho hlavní funkcí je řízení hovorů, tedy správa navázání, udržování a ukončení okruhově přepínaných spojení (kanálů pro přenos - B-kanály). Používá strukturu orientovanou na zprávy s klíčovými zprávami jako SETUP, CALL PROCEEDING, ALERTING, CONNECT a DISCONNECT. Kromě základního řízení hovorů podporuje DSS1 bohatou sadu doplňkových služeb prostřednictvím informačních prvků typu facility a specifických zpráv. Mezi ně patří přesměrování hovorů, čekání na hovor, prezentace/omezence identifikace volající linky ([CLIP](/mobilnisite/slovnik/clip/)/CLIR) a signalizace mezi uživateli (UUS).

V kontextech 3GPP byla role DSS1 především ve vzájemném propojení mezi mobilními jádrovými sítěmi (jako MSC) a pevnými ISDN sítěmi. Zatímco nativní mobilní signalizace 3GPP je založena na MAP (pro jádro) a RRC/NAS (pro přístup), DSS1 je odkazováno pro scénáře, kdy GSM/UMTS MSC potřebuje komunikovat s PSTN/ISDN pomocí ISDN User Part (ISUP) nebo přímo emulovat chování ISDN terminálu. Jeho zařazení do specifikací 3GPP (např. o účtování a vzájemném propojení) zajišťuje kompatibilitu a hladkou interoperabilitu s rozsáhlou instalovanou základnou pevné ISDN infrastruktury během přechodu na plně IP sítě.

## K čemu slouží

DSS1 vytvořila ITU za účelem poskytnutí standardizovaného, funkčně bohatého signalizačního systému pro ISDN, digitálního nástupce analogové PSTN. Jeho cílem bylo umožnit nejen základní hlasové hovory, ale také širokou škálu digitálních služeb (data, video, text) přes stejný účastnický přípojku, s přenesením signalizace z přenosového pásma na samostatný, vyhrazený D-kanál pro vyšší účinnost a flexibilitu.

V rámci 3GPP je na DSS1 odkazováno pro řešení problému vzájemného propojení mezi vznikajícími digitálními celulárními sítěmi a stávající infrastrukturou pevných digitálních sítí (ISDN). Mobilní sítě potřebovaly vůči ISDN účastníkům a ústřednám vystupovat jako ISDN nebo se s nimi spojovat, aby poskytovaly bezproblémové národní a mezinárodní roamování a směrování hovorů. Porozumění a podpora DSS1 umožnila systémům 3GPP nabízet kompatibilní doplňkové služby (jako identifikace volajícího) a využívat standardizované procedury pro navazování hovorů přes hranice sítí. Představuje klíčový prvek podpory starších protokolů, který zajišťoval zpětnou kompatibilitu během mnohaletého vývoje od okruhově přepínaných jader k paketově přepínaným plně IP jádřům (IMS).

## Klíčové vlastnosti

- Procedury řízení hovorů pro navázání a uvolnění okruhově přepínaných B-kanálů
- Podpora komplexní sady doplňkových služeb prostřednictvím informačních prvků
- Funguje nad spolehlivou spojovou vrstvou LAPD na ISDN D-kanálu
- Strukturovaná sada zpráv pro stavově řízené řízení hovorů (Q.931)
- Možnost signalizace mezi uživateli (UUS) pro omezený přenos dat
- Standardizované rozhraní (UNI) mezi uživatelským zařízením a ISDN ústřednou

## Související pojmy

- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)
- [LAPD – Link Access Procedure on the D-channel](/mobilnisite/slovnik/lapd/)
- [ISDN – Integrated Services Digital Network](/mobilnisite/slovnik/isdn/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 29.007** (Rel-19) — PLMN-PSTN/ISDN Interworking Requirements
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework

---

📖 **Anglický originál a plná specifikace:** [DSS1 na 3GPP Explorer](https://3gpp-explorer.com/glossary/dss1/)
