---
slug: "sct"
url: "/mobilnisite/slovnik/sct/"
type: "slovnik"
title: "SCT – Security Compliance Testing"
date: 2025-01-01
abbr: "SCT"
fullName: "Security Compliance Testing"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sct/"
summary: "SCT označuje soubor standardizovaných testovacích specifikací a metodologií definovaných 3GPP pro ověření implementace zabezpečení síťových prvků a uživatelských zařízení. Zajišťuje, že produkty splňu"
---

SCT je soubor standardizovaných testovacích specifikací a metodologií 3GPP používaných k ověření implementace zabezpečení a shody síťových prvků a uživatelských zařízení.

## Popis

Testování shody v oblasti zabezpečení (SCT) v rámci 3GPP zahrnuje komplexní rámec testovacích specifikací navržených k ověření, že implementace standardů 3GPP splňují definované bezpečnostní požadavky. Nejde o jediný test, ale o soubor metodologií a postupů dokumentovaných v různých technických specifikacích (TS). Testování pokrývá více vrstev a aspektů systému, včetně uživatelského zařízení (UE), rádiové přístupové sítě (RAN) a jádra sítě (CN). Proces zahrnuje jak testování shody, které kontroluje, zda implementace dodržuje standardy protokolů, tak bezpečnostní testování, které se konkrétně zaměřuje na bezpečnostní funkce a potenciální zranitelnosti.

Testovací metodologie často zahrnuje podrobné testovací případy, které simulují různé scénáře útoků a provozní podmínky, aby vyhodnotily odolnost bezpečnostních mechanismů. Mezi tyto mechanismy patří autentizace a dohoda o klíči ([AKA](/mobilnisite/slovnik/aka/)), ochrana integrity, šifrování, ochrana soukromí a zabezpečení přístupu k síti. Testovací specifikace definují požadované chování, sekvence zpráv a očekávané výsledky pro platné i neplatné vstupy. Testování lze provádět v laboratorních prostředích pomocí specializovaných testovacích zařízení, která emulují síťové komponenty nebo jiná uživatelská zařízení.

SCT je klíčové pro certifikační programy, kde musí produkty tyto testy úspěšně absolvovat, aby byly považovány za shodné a mohly být nasazeny v komerčních sítích. Specifikace jsou vyvíjeny pracovní skupinou pro zabezpečení 3GPP (SA3) ve spolupráci s dalšími skupinami a externími testovacími fóry, jako je Global Certification Forum ([GCF](/mobilnisite/slovnik/gcf/)) a PTCRB. Rozsah SCT se vyvíjí tak, aby pokrýval nové technologie, jako je 5G, kde zahrnuje testování vylepšeného soukromí účastníka ([SUCI](/mobilnisite/slovnik/suci/)), zabezpečení pro síťové segmenty (network slicing) a autentizaci v architekturách založených na službách.

## K čemu slouží

SCT bylo vytvořeno, aby řešilo kritickou potřebu standardizovaného, důsledného ověřování zabezpečení v mobilních sítích. Jak se sítě vyvíjely od 2G přes 3G a dále, jejich složitost a potenciální útočná plocha se výrazně zvýšily. Bez standardizovaného testování by různé implementace od různých dodavatelů mohly obsahovat bezpečnostní nedostatky nebo interpretovat standardy odlišně, což by vedlo ke zranitelnostem, problémům s interoperabilitou a potenciálním narušením sítě. SCT poskytuje společný referenční bod pro zajištění základní úrovně zabezpečení v celém ekosystému.

Řeší problém nekonzistentního a ad-hoc bezpečnostního testování tím, že poskytuje formální, podrobnou sadu požadavků, které musí výrobci splnit. To je nezbytné pro udržení důvěry uživatelů, ochranu dat účastníků a zajištění celkové integrity a dostupnosti síťových služeb. Motivace vychází z rostoucí závislosti na mobilních sítích pro citlivou komunikaci, finanční transakce a kritickou infrastrukturu, což činí robustní zabezpečení nezbytným. SCT pomáhá zmírňovat rizika spojená s novými technologiemi a složitými protokoly tím, že ověřuje implementace zabezpečení před jejich nasazením.

## Klíčové vlastnosti

- Standardizované testovací specifikace pro bezpečnostní protokoly 3GPP
- Ověření postupů autentizace a dohody o klíči (AKA)
- Testování algoritmů ochrany integrity a šifrování
- Vyhodnocení funkcí ochrany soukromí (např. ochrana IMSI)
- Testování shody pro signalizaci související se zabezpečením
- Podpora certifikace orgány jako GCF a PTCRB

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [GCF – Global Certification Forum](/mobilnisite/slovnik/gcf/)
- [SUCI – Subscription Concealed Identifier](/mobilnisite/slovnik/suci/)

## Definující specifikace

- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.852** (Rel-14) — MBMS user service profiles, APIs and transport enabler study
- **TR 26.946** (Rel-19) — MBMS User Services Overview
- **TS 33.805** (Rel-12) — 3GPP Network Product Security Assurance Methodology
- **TR 33.916** (Rel-19) — 3GPP Security Assurance Methodology (SECAM)

---

📖 **Anglický originál a plná specifikace:** [SCT na 3GPP Explorer](https://3gpp-explorer.com/glossary/sct/)
