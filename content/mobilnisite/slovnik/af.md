---
slug: "af"
url: "/mobilnisite/slovnik/af/"
type: "slovnik"
title: "AF – Authentication Framework"
date: 2026-01-01
abbr: "AF"
fullName: "Authentication Framework"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/af/"
summary: "Komplexní bezpečnostní rámec v sítích 3GPP, který poskytuje postupy pro autentizaci, autorizaci a dohodu klíčů (AKA). Navazuje vzájemnou autentizaci mezi uživatelským zařízením (UE) a sítí, čímž zajiš"
---

AF je komplexní bezpečnostní rámec 3GPP, který poskytuje postupy pro autentizaci, autorizaci a dohodu klíčů za účelem navázání vzájemné autentizace mezi uživatelským zařízením a sítí.

## Popis

Autentizační rámec (AF) je základním kamenem zabezpečení v sítích 3GPP a zahrnuje protokoly, algoritmy a postupy pro autentizaci uživatelů a síťových entit. Jeho jádrem je protokol Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)), který provádí vzájemnou autentizaci mezi uživatelským zařízením (UE) a jádrem sítě, konkrétně Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)) v 5G. Proces je založen na sdíleném tajném klíči (K) uloženém bezpečně v modulu [USIM](/mobilnisite/slovnik/usim/) v UE a v autentizačním centru (AuC) sítě. Rámec generuje relakční klíče pro šifrování a ochranu integrity uživatelských dat a signalizačních zpráv přes rozhraní rádiového přenosu.

Z architektonického hlediska AF integruje několik funkčních entit. UE a jeho USIM jsou klientské komponenty. V síti HSS/AuC generuje autentizační vektory ([AV](/mobilnisite/slovnik/av/)), z nichž každý obsahuje náhodnou výzvu ([RAND](/mobilnisite/slovnik/rand/)), očekávanou odpověď ([XRES](/mobilnisite/slovnik/xres/)), šifrovací klíč ([CK](/mobilnisite/slovnik/ck/)), integritní klíč (IK) a autentizační token (AUTN). Tyto vektory jsou odeslány do Mobility Management Entity (MME) obsluhující sítě v 4G nebo do Access and Mobility Management Function (AMF) v 5G. Obsluhující síť poté předá výzvu UE v podobě RAND a AUTN. USIM v UE ověří AUTN, aby autentizoval síť, vypočte svou odpověď (RES) a odvodí stejné CK a IK. Obsluhující síť porovná RES s XRES, čímž autentizuje UE.

Fungování rámce zahrnuje přesnou sekvenci. Nejprve obsluhující síť požádá domovskou síť o autentizační vektory. Po přijetí vektoru odešle RAND a AUTN do UE. USIM zkontroluje aktuálnost a pravost AUTN pomocí sekvenčních čísel (SQN) a kódů autentizace zpráv (MAC). Pokud jsou platné, USIM vypočte RES a klíče. UE odešle RES zpět, a pokud odpovídá XRES, je vzájemná autentizace úspěšná a odvozené klíče (CK, IK) jsou nainstalovány pro zabezpečení následné komunikační relace. V 5G se tento proces vyvinul do protokolů 5G AKA a EAP-AKA', které zavádějí separaci klíčů a vylepšenou kontrolu domovskou sítí.

Role AF přesahuje rámec počátečního přístupu. Podporuje správu bezpečnostního kontextu, umožňuje přeautentizaci a obnovu klíčů bez nutnosti plného běhu AKA při předávání spojení. Poskytuje také základ pro zabezpečení síťových řezů a umožňuje autentizaci pro přístup mimo 3GPP (např. přes Wi-Fi) prostřednictvím důvěryhodných nebo nedůvěryhodných rozhraní. Robustnost rámce spočívá v použití silných kryptografických algoritmů (MILENAGE, TUAK), ochraně proti útokům opakováním pomocí správy sekvenčních čísel a jasném oddělení dlouhodobého tajemství od provozních relakčních klíčů.

## K čemu slouží

Autentizační rámec byl vytvořen k řešení základního bezpečnostního problému v mobilních sítích: navázání důvěryhodného vztahu mezi mobilním zařízením a rozsáhlou, distribuovanou sítí provozovanou více subjekty. Před standardizovanou autentizací v digitálních mobilních systémech (jako GSM) měly analogové systémy prakticky žádnou bezpečnost, což je činilo zranitelnými vůči klonování a odposlechu. Počáteční rámec v GSM zavedl jednosměrnou autentizaci (síť autentizuje účastníka), ale později byl shledán zranitelným vůči útokům falešných základnových stanic. Vytvoření 3GPP AF s UMTS (Release 99/4) bylo motivováno potřebou vzájemné autentizace a silnějších kryptografických algoritmů pro umožnění zabezpečených mobilních datových služeb, elektronického obchodu a podnikového přístupu.

Rámec řeší kritická omezení předchozích přístupů. Algoritmy A3/A8 v GSM byly slabé a poskytovaly pouze jednosměrnou autentizaci. 3GPP AF zavedl vzájemnou autentizaci prostřednictvím tokenu AUTN, což umožnilo UE ověřit legitimitu sítě, a tím zmírnit útoky typu man-in-the-middle. Také posílil odvozování klíčů, zvýšil délky klíčů a zavedl ochranu integrity (IK) vedle šifrování (CK). To bylo zásadní, protože se sítě vyvíjely z primárně hlasových na přenášející citlivá data. Koncepce rámce také řeší problém zabezpečeného roamingu definováním toho, jak obsluhující (navštívená) síť může autentizovat uživatele pomocí přihlašovacích údajů a postupů řízených domovskou sítí, čímž vytváří globální model důvěry.

Jeho vývoj je dále poháněn novými hrozbami a požadavky služeb. Přechod na plně IP sítě (EPS v 4G) a cloudové architektury (5GC v 5G) přinesl nové vektory útoků. AF se přizpůsobil vylepšením hierarchie klíčů (např. zavedením K_ASME v 4G a KAUSF v 5G pro separaci klíčů mezi síťovými vrstvami), podporou nových autentizačních protokolů jako EAP a integrací s rámci správy identit. Poskytuje nezbytný důvěryhodný kotvící bod pro síťové řezy, hromadnou konektivitu IoT a edge computing, čímž zajišťuje, že se zabezpečení škáluje a přizpůsobuje síťové architektuře.

## Klíčové vlastnosti

- Vzájemná autentizace mezi UE a sítí prostřednictvím protokolu AKA
- Generování šifrovacího klíče (CK) a integritního klíče (IK) pro zabezpečení relace
- Použití sdíleného dlouhodobého tajemství (K) uloženého v USIM a HSS/AuC
- Ochrana proti útokům opakováním prostřednictvím správy sekvenčních čísel (SQN)
- Podpora agilnosti algoritmů (např. MILENAGE, TUAK) a aktualizace klíčů
- Základ pro zabezpečený roaming a autentizaci v obsluhujících sítích

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)

## Definující specifikace

- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 23.139** (Rel-19) — 3GPP-Fixed Broadband Interworking Stage 2
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.287** (Rel-19) — 5G V2X Architecture Enhancements
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.433** (Rel-20) — SEAL Data Delivery (SEALDD) for Verticals
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- … a dalších 81 specifikací

---

📖 **Anglický originál a plná specifikace:** [AF na 3GPP Explorer](https://3gpp-explorer.com/glossary/af/)
