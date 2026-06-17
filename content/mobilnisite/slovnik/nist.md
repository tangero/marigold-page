---
slug: "nist"
url: "/mobilnisite/slovnik/nist/"
type: "slovnik"
title: "NIST – National Institute of Standards and Technology"
date: 2025-01-01
abbr: "NIST"
fullName: "National Institute of Standards and Technology"
category: "Other"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/nist/"
summary: "Neregulační agentura Ministerstva obchodu Spojených států amerických, NIST vyvíjí a prosazuje měřicí standardy a technologie. V kontextu 3GPP je její eliptická křivka P256 referencována jako kryptogra"
---

NIST je Národní institut pro standardy a technologie Spojených států amerických, neregulační agentura, jejíž eliptická křivka P256 je referenčním kryptografickým standardem pro zabezpečení sítí 5G v rámci 3GPP.

## Popis

Ve standardech 3GPP je Národní institut pro standardy a technologie (NIST) referencován jako zdroj specifických kryptografických standardů a algoritmů používaných pro zajištění zabezpečení sítě. Nejvýznamněji je eliptická křivka P-256 definovaná NIST (známá také jako secp256r1 nebo prime256v1) přijata jako standardní kryptografický primitiv. Tato křivka je využívána v protokolu 5G Authentication and Key Agreement (5G [AKA](/mobilnisite/slovnik/aka/)) a v ověřovacím rámci EAP-AKA' pro generování klíčového materiálu a zajištění vzájemného ověření mezi uživatelským zařízením (UE) a sítí.

Technická integrace zahrnuje použití eliptické křivky P-256 pro operace eliptické křivkové kryptografie ([ECC](/mobilnisite/slovnik/ecc/)). V 5G používají Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)) domovské sítě i UE sdílený dlouhodobý tajný klíč (K) uložený na modulu USIM a v Authentication Credential Repository and Processing Function ([ARPF](/mobilnisite/slovnik/arpf/)) v domovské síti. Během primárního ověřování je tento sdílený tajemství použit ve spojení s ECC založenou na křivce NIST P-256 pro generování relačních klíčů a poskytnutí kryptografického důkazu identity. Použití standardizované a důkladně prověřené křivky, jako je P-256, zajišťuje pevný základ pro utajení a integritu následné komunikace.

Role standardů NIST v 3GPP spočívá v poskytování důvěryhodné, veřejně dostupné a rigorózně hodnocené sady kryptografických algoritmů. To je klíčové pro interoperabilitu a globální záruku zabezpečení. Odkazováním na standardy NIST se 3GPP vyhýbá návrhu vlastní proprietární kryptografie, která by mohla zavést zranitelnosti. Místo toho využívá algoritmy, které prošly rozsáhlým veřejným posouzením globální kryptografické komunity. Konkrétní dokument 3GPP TS 35.934 podrobně popisuje implementaci a použití těchto eliptických křivek schválených NIST v rámci bezpečnostní architektury 3GPP.

Mimo křivku P-256 širší role NIST při definování standardů pro kryptografické hašovací funkce (jako SHA-256), generování náhodných čísel a dalších bezpečnostních směrnic nepřímo ovlivňuje návrh bezpečnostních protokolů 3GPP. Spoléhání se na takové zavedené standardy je základním principem zabezpečení v 3GPP, který zajišťuje, že mobilní ekosystém těží z nejmodernější, mezinárodně uznávané kryptografické ochrany.

## K čemu slouží

Zařazení standardů NIST do specifikací 3GPP slouží kritickému účelu poskytnutí robustního, ověřitelného a interoperabilního kryptografického základu pro zabezpečení mobilních sítí. Kryptografie je základem bezpečné komunikace, chrání soukromí uživatelů, integritu sítě a majetek operátorů. Návrh proprietárních, neprověřených kryptografických algoritmů nese obrovské riziko, protože skryté chyby mohou vést ke katastrofálním bezpečnostním průlomům. Přijetím dobře zavedených standardů od renomované organizace, jako je NIST, 3GPP zajišťuje, že bezpečnostní mechanismy v miliardách zařízení prošly důkladným odborným posouzením a jsou odolné vůči známým útokům.

Historický kontext je takový, že dřívější mobilní generace (2G, 3G) používaly operátorsky specifické nebo méně transparentní kryptografické algoritmy, které v průběhu času čelily různým kritikám a zranitelnostem. Pro 5G klade 3GPP silný důraz na vylepšené zabezpečení, včetně flexibility algoritmů a transparentnosti. Odkazování na veřejně dostupné standardy NIST je v souladu s tímto cílem. Umožňuje nezávislé ověření implementací, podporuje globální přijetí (protože standardy NIST jsou široce přijímány) a usnadňuje soulad s různými národními a mezinárodními bezpečnostními předpisy.

Konkrétně volba eliptické křivky NIST P-256 řeší potřebu efektivní a silné kryptografie s veřejným klíčem. Eliptická křivková kryptografie nabízí ekvivalentní zabezpečení jako tradiční RSA s mnohem menšími velikostmi klíčů, což je klíčové pro zařízení s omezenými zdroji a pro snížení signalizační režie. Křivka P-256 poskytuje úroveň zabezpečení 128 bitů, která je považována za bezpečnou proti současným výpočetním hrozbám. Její standardizace NIST z ní činí bezpečnou, efektivní a globálně uznávanou volbu pro procedury ověřování a dohody klíčů, které chrání každé 5G připojení.

## Klíčové vlastnosti

- Poskytuje standardizovanou eliptickou křivku NIST P-256 (secp256r1) pro kryptografii 5G
- Umožňuje silné vzájemné ověření mezi UE a sítí v 5G AKA
- Podporuje generování bezpečných relačních klíčů pro ochranu důvěrnosti a integrity
- Zajišťuje transparentnost algoritmů a veřejné posouzení prostřednictvím publikací NIST
- Podporuje globální interoperabilitu bezpečnostních implementací
- Nabízí efektivní kryptografii s menšími velikostmi klíčů ve srovnání s tradičním RSA

## Související pojmy

- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)

## Definující specifikace

- **TR 35.934** (Rel-19) — Tuak algorithm set for 3GPP auth & key gen

---

📖 **Anglický originál a plná specifikace:** [NIST na 3GPP Explorer](https://3gpp-explorer.com/glossary/nist/)
