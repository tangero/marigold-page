---
slug: "pkcs"
url: "/mobilnisite/slovnik/pkcs/"
type: "slovnik"
title: "PKCS – Public-Key Cryptography Standards"
date: 2025-01-01
abbr: "PKCS"
fullName: "Public-Key Cryptography Standards"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/pkcs/"
summary: "PKCS označuje soubor standardů interoperability pro kryptografii s veřejným klíčem, původně vyvinutých společností RSA Laboratories a široce přijatých. V rámci 3GPP tyto standardy definují formáty a p"
---

PKCS je soubor široce přijímaných standardů interoperability, které definují formáty a protokoly pro bezpečnou správu klíčů, šifrování, digitální podpisy a manipulaci s certifikáty v sítích 3GPP a na UICC.

## Popis

Public-Key Cryptography Standards (PKCS) jsou souborem specifikací, které definují formáty, algoritmy a protokoly pro nasazení kryptografie s veřejným klíčem. Ačkoli je původně vyvinula společnost [RSA](/mobilnisite/slovnik/rsa/) Security, staly se de facto i de jure standardy, které jsou v technických specifikacích 3GPP hojně odkazovány, aby zajistily interoperabilitu mezi zařízeními a systémy různých dodavatelů. PKCS pokrývají širokou škálu kryptografických operací nezbytných pro moderní telekomunikační zabezpečení.

V architektuře 3GPP jsou různé standardy PKCS využívány v různých síťových prvcích a bezpečnostních modulech. Klíčovou součástí je Universal Integrated Circuit Card (UICC), kde PKCS#15 definuje souborový systém a bezpečnostní strukturu pro ukládání kryptografických objektů, jako jsou soukromé klíče, certifikáty a datové objekty. To umožňuje standardizovaný přístup k bezpečnostním přihlašovacím údajům na čipové kartě. PKCS#1 definuje schémata RSA šifrování a podpisu, která jsou zásadní pro zabezpečení signalizace a uživatelských dat. PKCS#7 a PKCS#12 definují formáty pro kryptografické zprávy a výměnu osobních informací, používané při transportu certifikátů a klíčů.

Fungování PKCS v systémech 3GPP zahrnuje standardizované datové struktury a pravidla zpracování. Například když síťová funkce potřebuje ověřit digitální podpis na protokolové zprávě, použije formát podpisu a schéma doplňování (padding) specifikované v PKCS#1. Když poskytovatel služeb provizionuje certifikát na UICC, může použít balíček PKCS#12. Úlohou PKCS je poskytnout základní, dodavatelsky neutrální kryptografické 'stavební bloky', které umožňují bezpečné bootstrapování, autentizaci (jako v [AKA](/mobilnisite/slovnik/aka/)), zabezpečenou výměnu zpráv a správu přihlašovacích údajů v celém ekosystému 3GPP, od uživatelského zařízení (UE) po jádro sítě.

## K čemu slouží

PKCS byly vytvořeny, aby vyřešily kritický problém interoperability v kryptografii s veřejným klíčem. Před těmito standardy různí dodavatelé implementovali kryptografické funkce – generování klíčů, šifrování, digitální podpisy – proprietárními a nekompatibilními způsoby. To znemožňovalo vybudování heterogenních, vícedodavatelských sítí, kde by zařízení jednoho výrobce muselo bezpečně komunikovat se síťovým zařízením jiného. Přijetí PKCS v rámci 3GPP bylo motivováno potřebou spolehlivé, ověřené a široce přijímané sady specifikací, které by tvořily základ bezpečnostní architektury.

Historický kontext představuje přechod k sofistikovanějším bezpečnostním mechanismům přesahujícím sdílené tajné klíče. Jak se sítě 3GPP vyvíjely, aby podporovaly elektronické obchodování, zákonné odposlechy a pokročilou autentizaci, vyžadovaly robustní infrastrukturu veřejných klíčů ([PKI](/mobilnisite/slovnik/pki/)). PKCS poskytly hotová, standardizovaná řešení pro tyto potřeby. Odstraňují omezení ad-hoc implementací tím, že poskytují rigorózně definované formáty pro klíče (PKCS#1, #8), certifikáty (součást PKCS#7) a zabezpečené kontejnery (PKCS#12). To umožňuje bezpečné nasazení a správu přihlašovacích údajů na UICC, v síťových uzlech a na aplikačních serverech, čímž vytváří konzistentní základ důvěry v celosvětové mobilní síti.

## Klíčové vlastnosti

- Definuje standardní formáty pro veřejné a soukromé klíče RSA (PKCS#1)
- Specifikuje syntax kryptografických zpráv pro podpisy a šifrování (PKCS#7)
- Poskytuje standard pro výměnu osobních informací (PKCS#12)
- Definuje standard rozhraní pro kryptografické tokeny (PKCS#11)
- Specifikuje souborový systém a bezpečnostní strukturu pro čipové karty (PKCS#15)
- Zajišťuje interoperabilitu kryptografických funkcí ve vícedodavatelských sítích

## Související pojmy

- [RSA – Rivest-Shamir-Adleman](/mobilnisite/slovnik/rsa/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 33.221** (Rel-19) — Subscriber Certificate Distribution via GBA
- **TS 33.310** (Rel-19) — 3GPP Authentication Framework for Network Nodes
- **TS 33.812** (Rel-9) — M2M Remote Subscription Management Security
- **TR 33.876** (Rel-18) — Technical Report on Certificate Management

---

📖 **Anglický originál a plná specifikace:** [PKCS na 3GPP Explorer](https://3gpp-explorer.com/glossary/pkcs/)
