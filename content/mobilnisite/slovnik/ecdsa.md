---
slug: "ecdsa"
url: "/mobilnisite/slovnik/ecdsa/"
type: "slovnik"
title: "ECDSA – Elliptic Curve Digital Signature Algorithm"
date: 2025-01-01
abbr: "ECDSA"
fullName: "Elliptic Curve Digital Signature Algorithm"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/ecdsa/"
summary: "ECDSA je kryptografický algoritmus pro generování digitálních podpisů využívající kryptografii eliptických křivek. Poskytuje autentizaci, integritu dat a nepopiratelnost s kratšími délkami klíčů než t"
---

ECDSA je kryptografický algoritmus pro generování digitálních podpisů využívající kryptografii eliptických křivek, který poskytuje autentizaci, integritu dat a nepopiratelnost s efektivnějšími, kratšími délkami klíčů a je široce používán ve specifikacích 3GPP pro zabezpečení síťové signalizace a autentizace.

## Popis

Elliptic Curve Digital Signature Algorithm (ECDSA) je standard asymetrické kryptografie pro vytváření digitálních podpisů. Je založen na algebraické struktuře eliptických křivek nad konečnými tělesy. V ECDSA má každý subjekt privátní klíč (náhodně vybrané celé číslo) a odpovídající veřejný klíč (bod na eliptické křivce odvozený z privátního klíče). Algoritmus využívá jako svůj základní obtížný problém problém diskrétního logaritmu na eliptické křivce (ECDLP), který je považován za výpočetně neproveditelný.

Proces podepisování využívá podepisovatelův privátní klíč a kryptografický hash zprávy. Podepisovatel pro každý podpis vygeneruje náhodný efemérní pár klíčů. Pomocí privátního klíče, efemérního privátního klíče a hashe zprávy algoritmus vypočítá dvě celá čísla, 'r' a 's', která tvoří podpis. Proces ověření využívá podepisovatelův veřejný klíč, hash zprávy a podpis (r, s). Ověřovatel provede sérii operací s body eliptické křivky, aby zkontroloval, zda platí odvozená rovnice. Pokud ano, je podpis platný, což dokazuje, že zprávu podepsal držitel privátního klíče a že nebyla změněna.

V rámci architektury 3GPP je ECDSA integrován do několika klíčových bezpečnostních protokolů a funkcí. Je specifikován jako podporovaný algoritmus pro vylepšení Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)), pro autentizaci založenou na certifikátech v 5G a pro integritní ochranu signalizačních zpráv. Například v 5G lze ECDSA použít pro digitální podpisy při výpočtu [SUCI](/mobilnisite/slovnik/suci/) (Subscription Concealed Identifier) a pro podpisy důkazů o atestaci platformy v konceptech jako [SEAL](/mobilnisite/slovnik/seal/) (Secure Environment for Applications Loaded).

Klíčové součásti implementace v 3GPP zahrnují výběr konkrétní eliptické křivky (např. [NIST](/mobilnisite/slovnik/nist/) P-256, Brainpool křivky), hashovací funkce (např. SHA-256) a přesné kódování podpisů. Úlohou algoritmu je poskytovat silnou autentizaci (prokázání identity síťové funkce nebo UE), integritu dat (zajištění, že signalizační zprávy nebyly pozměněny) a nepopiratelnost (podepisovatel se nemůže následně zříct, že podpis vytvořil). Jeho efektivita jej činí vhodným pro prostředí s omezenými zdroji, jako jsou zařízení IoT, a pro scénáře signalizace s vysokým objemem v 5G core sítích.

## K čemu slouží

ECDSA byl zaveden, aby řešil neefektivnost předchozích schémat digitálních podpisů, především [RSA](/mobilnisite/slovnik/rsa/). Zatímco zabezpečení RSA závisí na obtížnosti faktorizace velkých celých čísel, dosažení vysoké úrovně zabezpečení vyžaduje velmi dlouhé klíče (např. 2048 nebo 4096 bitů), což vede k velkým podpisům, vysoké výpočetní zátěži a významné spotřebě přenosové kapacity. ECDSA byl vytvořen, aby poskytoval srovnatelné nebo vyšší zabezpečení s mnohem menšími velikostmi klíčů (např. 256bitový klíč [ECC](/mobilnisite/slovnik/ecc/) nabízí zabezpečení srovnatelné s 3072bitovým klíčem RSA).

Historická motivace v rámci 3GPP vychází z potřeby silnější a efektivnější kryptografie s vývojem sítí. Systémy před 4G se silně spoléhaly na symetrickou kryptografii a certifikáty založené na RSA pro [PKI](/mobilnisite/slovnik/pki/) core sítě. S nástupem 4G LTE a zejména 5G se rozšířil model hrozeb a počet zařízení (IoT) explodoval. Výpočetní náročnost a nároky na přenosovou kapacitu u RSA se staly omezujícím faktorem. ECDSA tento problém řeší tím, že umožňuje rychlejší generování/ověřování podpisů, menší velikosti certifikátů (snížení režie pro ukládání a přenos) a nižší spotřebu energie – což je klíčové pro bateriově napájená zařízení IoT.

ECDSA navíc efektivněji než RSA řeší potřebu přípravy na budoucí hrozby kvantových počítačů, ačkoli oba algoritmy jsou zranitelné vůči Shorovu algoritmu. Kratší délky klíčů systémů založených na ECC mohou učinit přechod na post-kvantovou kryptografii (PQC) potenciálně lépe zvládnutelným. V 3GPP bylo jeho přijetí, počínaje Release 12, hnáno těmito zisky v efektivitě a snahou o soulad s globálními osvědčenými postupy v kryptografii (např. doporučení [NIST](/mobilnisite/slovnik/nist/)), což umožňuje silnější autentizaci síťových funkcí, certifikátů UE a procesů secure bootu škálovatelným způsobem.

## Klíčové vlastnosti

- Kratší délky klíčů: Poskytuje silné zabezpečení (např. 256bitové) srovnatelné s mnohem delšími klíči RSA.
- Výpočetní efektivita: Rychlejší generování a ověřování podpisů než u RSA při srovnatelné úrovni zabezpečení.
- Malá velikost podpisu: Vytváří kompaktní podpisy, což snižuje režii protokolů.
- Standardizované křivky: Podporuje mezinárodně uznávané křivky jako NIST P-256, P-384 a Brainpool.
- Široké průmyslové přijetí: Nedílná součást moderního PKI, blockchainu a mnoha internetových standardů.
- Základ pro pokročilé protokoly: Používá se v 3GPP pro ochranu SUCI, autentizaci pomocí certifikátů a integritu platformy.

## Související pojmy

- [ECIES – Elliptic Curve Integrated Encryption Scheme](/mobilnisite/slovnik/ecies/)

## Definující specifikace

- **TS 33.303** (Rel-19) — ProSe Security Specification for EPS
- **TS 33.885** (Rel-14) — Security Study for V2X Services
- **TR 33.938** (Rel-19) — 3GPP Cryptographic Inventory for 5G
- **TR 33.969** (Rel-19) — Security for Public Warning System (PWS)

---

📖 **Anglický originál a plná specifikace:** [ECDSA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ecdsa/)
