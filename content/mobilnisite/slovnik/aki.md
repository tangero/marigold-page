---
slug: "aki"
url: "/mobilnisite/slovnik/aki/"
type: "slovnik"
title: "AKI – Asymmetric Key Index"
date: 2025-01-01
abbr: "AKI"
fullName: "Asymmetric Key Index"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/aki/"
summary: "AKI je bezpečnostní parametr používaný v sítích 3GPP k identifikaci toho, který veřejný klíč z páru má být použit pro autentizaci nebo šifrování. Je nezbytný pro správu více kryptografických klíčů v m"
---

AKI je bezpečnostní parametr používaný v sítích 3GPP k identifikaci toho, který veřejný klíč z páru má být použit pro autentizaci nebo šifrování.

## Popis

Asymmetric Key Index (AKI) je klíčový bezpečnostní parametr definovaný ve specifikacích 3GPP, především v kontextu aplikací UICC (Universal Integrated Circuit Card) a USIM (Universal Subscriber Identity Module). Funguje jako identifikátor, který odkazuje na konkrétní veřejný klíč v rámci asymetrického páru klíčů uloženého na kartě. V praxi, když síťová entita (jako Home Subscriber Server - [HSS](/mobilnisite/slovnik/hss/)) potřebuje autentizovat USIM nebo navázat zabezpečený kanál, musí vědět, který veřejný klíč použít z několika potenciálně dostupných na kartě. AKI poskytuje tuto referenci, přičemž jde typicky o jednobytovou hodnotu (0-255), která odpovídá konkrétnímu indexu páru klíčů v souborovém systému USIM.

Z architektonického hlediska je AKI zabudován do bezpečnostních datových struktur, nejvýznamněji do Authentication Vector ([AV](/mobilnisite/slovnik/av/)) používaného v proceduře [AKA](/mobilnisite/slovnik/aka/) (Authentication and Key Agreement). Když HSS generuje AV pro účastníka, zahrne hodnotu AKI, aby informovala obsluhující síť (např. [MSC](/mobilnisite/slovnik/msc/), SGSN, [MME](/mobilnisite/slovnik/mme/)), na který klíč infrastruktury veřejných klíčů (PKI) se má odkazovat, pokud jsou použity metody autentizace založené na certifikátech, nebo pro zabezpečenou komunikaci. USIM při přijetí výzvy použije AKI k výběru správného privátního klíče pro generování odpovědi nebo dešifrování informací. Tento mechanismus je zásadní pro scénáře, kdy má stejný USIM klíče více poskytovatelů služeb nebo síťových operátorů, nebo během období přechodu na nové klíče, kdy staré a nové klíče koexistují.

Jeho role přesahuje základní autentizaci. V architektuře Generic Bootstrapping Architecture ([GBA](/mobilnisite/slovnik/gba/)) lze AKI použít k identifikaci správného klíčového materiálu pro zabezpečení aplikací při inicializaci. V kontextu bezpečnostní architektury 3GPP definované v TS 33.102 a specifikací aplikací UICC jako TS 31.102 AKI zajišťuje, že kryptografické operace jsou prováděny s určeným párem klíčů, čímž udržuje řetězec důvěry. Správa hodnot AKI je přísně kontrolována prostřednictvím [OTA](/mobilnisite/slovnik/ota/) (Over-The-Air) platforem a procesů personalizace karet, což zajišťuje, že síťoví operátoři mohou bezpečně aktualizovat a spravovat kryptografické klíče na nasazených kartách SIM/USIM bez přerušení služeb.

## K čemu slouží

AKI byl zaveden k řešení problému správy více asymetrických kryptografických klíčů na jedné USIM kartě. Před jeho standardizací používaly karty SIM typicky symetrické klíčové algoritmy (jako COMP128) pro autentizaci, kdy byl jediný tajný klíč (Ki) sdílen mezi kartou a sítí. S vývojem směrem k bezpečnějším mechanismům založeným na PKI pro aplikace jako digitální podpisy, zabezpečené [OTA](/mobilnisite/slovnik/ota/) aktualizace a vylepšené autentizační protokoly vznikla potřeba ukládat několik párů veřejných/privátních klíčů na kartě. Bez indexu neměla síť způsob, jak určit, který klíč použít pro danou operaci, což vedlo k potenciální nejednoznačnosti a selhání autentizace.

Historicky, jak se sítě 3GPP vyvíjely od 2G přes 3G (UMTS) a dále, se bezpečnostní požadavky zpřísnily. Zavedení USIM v 3G vyžadovalo podporu silnějších autentizačních algoritmů a možnost přidružených služeb vyžadujících PKI. AKI poskytl jednoduchý, efektivní mechanismus pro odkazování na správný klíč, což umožnilo funkce jako síťová autentizace pomocí certifikátů, zabezpečené poskytování aplikací a podpora přihlašovacích údajů více poskytovatelů služeb na jedné kartě. Vyřešil omezení statického, jediného páru klíčů tím, že umožnil dynamickou správu klíčů a operace životního cyklu, jako je obnova nebo odvolání klíčů, bez výměny fyzické karty SIM.

AKI navíc usnadňuje interoperabilu v prostředích více operátorů (např. roaming) a pro komunikaci typu stroj-stroj (M2M), kde může UICC zařízení obsahovat klíče pro různé síťové profily nebo aplikace. Zahrnutím AKI do autentizačních vektorů a signalizačních zpráv zajišťuje, že síť i USIM jsou synchronizovány v aktivním kryptografickém kontextu, což zabraňuje bezpečnostním narušením a odmítnutí služeb, ke kterým by mohlo dojít při neshodě klíčů. Jeho vytvoření bylo motivováno potřebou škálovatelné, budoucím vývojem odolné bezpečnosti, která by dokázala pojmout vyvíjející se kryptografické standardy a rostoucí složitost mobilních služeb.

## Klíčové vlastnosti

- Jednoznačně identifikuje asymetrický pár klíčů v rámci souborového systému USIM
- Umožňuje podporu více PKI klíčů na jedné UICC pro různé služby nebo operátory
- Integruje se do Authentication Vectors (AV) pro síťem řízený výběr klíče během AKA
- Umožňuje bezpečnou správu životního cyklu klíčů včetně aktualizací a přechodů prostřednictvím OTA
- Podporuje Generic Bootstrapping Architecture (GBA) identifikací správného klíčového materiálu
- Zajišťuje interoperabilitu v scénářích roamingu a UICC s více aplikacemi

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification

---

📖 **Anglický originál a plná specifikace:** [AKI na 3GPP Explorer](https://3gpp-explorer.com/glossary/aki/)
