---
slug: "auc"
url: "/mobilnisite/slovnik/auc/"
type: "slovnik"
title: "AUC – Authentication Centre"
date: 2026-01-01
abbr: "AUC"
fullName: "Authentication Centre"
category: "Security"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/auc/"
summary: "Authentication Centre (AUC) je bezpečnostní entita základní sítě, která generuje autentizační vektory (trojice/pětice) pro ověření účastníka. Bezpečně ukládá autentizační klíče účastníků (Ki) a krypto"
---

AUC je bezpečnostní entita základní sítě, která generuje autentizační vektory a bezpečně ukládá klíče účastníků, aby umožnila bezpečné ověřování účastníků a zabránila neoprávněnému přístupu v mobilních sítích 3GPP.

## Popis

Authentication Centre (AUC) je kritická bezpečnostní komponenta v architektuře sítě 3GPP, primárně odpovědná za autentizaci účastníka a generování klíčů. Funguje jako zabezpečená databáze, která ukládá dlouhodobý tajný klíč (Ki) pro každého účastníka spolu s kryptografickými algoritmy používanými k tvorbě autentizačních vektorů. Tyto vektory jsou následně poskytnuty Visitor Location Register ([VLR](/mobilnisite/slovnik/vlr/)) nebo Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) k ověření mobilních zařízení pokoušejících se o přístup do sítě.

Architektonicky je AUC typicky integrována s Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) jako součást Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) v evolučních sítích 3GPP, ačkoli může existovat jako samostatná fyzická entita. AUC obsahuje autentizační klíč (Ki), což je 128bitový tajný klíč jedinečný pro [SIM](/mobilnisite/slovnik/sim/) kartu každého účastníka, a implementuje kryptografické algoritmy jako [A3](/mobilnisite/slovnik/a3/) pro autentizaci, [A8](/mobilnisite/slovnik/a8/) pro generování šifrovacího klíče (v GSM) a MILENAGE (pro UMTS/LTE/5G). Když se účastník pokusí o přístup do sítě, obsluhující síť požádá o autentizační vektory z AUC/HLR, které je vygenerují pomocí účastníkova klíče Ki a náhodné výzvy (RAND).

Autentizační proces začíná, když Mobile Switching Centre (MSC) nebo SGSN požádá o autentizační data z HLR/AUC. AUC vygeneruje autentizační vektor obsahující: náhodné číslo (RAND), očekávanou odpověď (XRES) vypočítanou pomocí algoritmu A3 s Ki a RAND, šifrovací klíč (Kc) vygenerovaný pomocí algoritmu A8 a v sítích UMTS/LTE/5G další prvky jako autentizační token (AUTN) a relakční klíče. Tento vektor je odeslán do obsluhující sítě, která přepošle RAND do mobilního zařízení. Mobilní zařízení vypočte vlastní odpověď (SRES) pomocí stejného Ki a algoritmu A3, kterou síť porovná s XRES pro účely autentizace.

Pro UMTS a novější technologie AUC generuje pětice namísto trojic, přidávajíc do vektoru autentizační token (AUTN) a integritní klíč (IK). AUTN umožňuje oboustrannou autentizaci, při které mobilní zařízení ověřuje autentičnost sítě. AUC také podporuje odvozování klíčů pro následné bezpečnostní procedury, generuje šifrovací klíče (CK) a integritní klíče (IK) pro zabezpečenou komunikaci. V sítích 5G je funkce AUC plně integrována do Unified Data Management (UDM) a Authentication Server Function (AUSF), ale zachovává stejný základní účel generování autentizačních vektorů.

Bezpečnostní architektura AUC zajišťuje, že Ki nikdy neopustí zabezpečené prostředí, čímž zabraňuje jeho odhalení během autentizace. Všechny kryptografické výpočty probíhají uvnitř chráněného rozhraní AUC a pouze vygenerované autentizační vektory jsou přenášeny do síťových prvků. Tento konstrukční princip zachovává důvěrnost dlouhodobého tajného klíče a zároveň umožňuje bezpečnou autentizaci v celé síti.

## K čemu slouží

Authentication Centre byl vytvořen, aby řešil základní bezpečnostní zranitelnosti v raných mobilních sítích, kterým chyběly robustní autentizační mechanismy. Před standardizací GSM trpěly analogové mobilní systémy podvody s klonováním, kdy útočníci mohli zachytit a replikovat identifikátory účastníků. AUC zavedlo kryptografický autentizační rámec, který ověřoval identitu účastníka a zároveň chránil síťové zdroje před neoprávněným přístupem.

Primární problém, který AUC řeší, je bezpečná autentizace účastníka pomocí kryptografických mechanismů výzva-odpověď. Ukládáním tajného autentizačního klíče (Ki) v zabezpečeném síťovém prvku namísto jeho přenosu AUC zabraňuje zachycení klíče a útokům přehráním. Tento přístup také umožňuje generování relakčně specifických šifrovacích klíčů (Kc) pro šifrovanou komunikaci, čímž řeší zranitelnosti odposlechu v rádiovém přenosu.

Historicky bylo vytvoření AUC motivováno potřebou standardizované bezpečnosti v mezinárodních roamingových scénářích. Jak se GSM globálně rozšiřovalo, byl vyžadován konzistentní autentizační mechanismus, který by mohl fungovat napříč různými síťovými operátory při zachování bezpečnosti. Centralizovaná správa klíčů a generování vektorů AUC poskytly tuto konzistenci a vytvořily základ pro následné bezpečnostní architektury 3GPP včetně autentizace a dohody o klíči (AKA) v UMTS a autentizace v evolučním paketovém systému v LTE/5G.

## Klíčové vlastnosti

- Generuje autentizační vektory (trojice pro GSM, pětice pro UMTS+) pomocí uloženého Ki a kryptografických algoritmů
- Bezpečně ukládá autentizační klíče účastníků (Ki) v chráněném prostředí, které brání externímu přístupu
- Implementuje více kryptografických algoritmů včetně A3/A8 pro GSM a MILENAGE pro sítě UMTS/LTE/5G
- Podporuje oboustrannou autentizaci v sítích UMTS+ prostřednictvím generování autentizačního tokenu (AUTN)
- Generuje relakční klíče (Kc, CK, IK) pro šifrování a integritní ochranu komunikace
- Integruje se s HLR/HSS/UDM pro centralizovanou správu bezpečnosti účastníků napříč generacemi sítí

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)
- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [SIM – Subscriber Identity Module / Universal Subscriber Identity Module](/mobilnisite/slovnik/sim/)

## Definující specifikace

- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 28.622** (Rel-20) — Telecommunication Management; Generic NRM Information Service
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.622** (Rel-11) — Generic Network Resources IRP NRM
- **TS 32.632** (Rel-11) — Core Network Resources IRP: Network Resource Model
- **TS 32.732** (Rel-11) — IMS Network Resource Model IRP: Information Service
- **TR 33.848** (Rel-18) — Technical Report on Virtualisation Security

---

📖 **Anglický originál a plná specifikace:** [AUC na 3GPP Explorer](https://3gpp-explorer.com/glossary/auc/)
