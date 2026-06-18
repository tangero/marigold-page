---
slug: "ecies"
url: "/mobilnisite/slovnik/ecies/"
type: "slovnik"
title: "ECIES – Elliptic Curve Integrated Encryption Scheme"
date: 2025-01-01
abbr: "ECIES"
fullName: "Elliptic Curve Integrated Encryption Scheme"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/ecies/"
summary: "ECIES je hybridní šifrovací schéma kombinující kryptografii eliptických křivek pro dohodu klíče se symetrickým šifrováním pro důvěrnost dat. Používá se v 3GPP pro zabezpečení protokolů, jako je přenos"
---

ECIES je hybridní šifrovací schéma, které využívá kryptografii eliptických křivek pro dohodu klíče a symetrické šifrování pro důvěrnost dat, používané v 3GPP pro zabezpečení protokolů, jako je přenos 5G NAS.

## Popis

Schéma integrovaného šifrování na bázi eliptických křivek (ECIES) je šifrovací schéma s veřejným klíčem standardizované více orgány, včetně SECG a [ISO](/mobilnisite/slovnik/iso/), a přijaté 3GPP pro specifické bezpečnostní funkce. Jedná se o hybridní kryptosystém, což znamená, že efektivně kombinuje asymetrické a symetrické kryptografické techniky. Schéma využívá kryptografii eliptických křivek ([ECC](/mobilnisite/slovnik/ecc/)) pro část zapouzdření klíče (key encapsulation) k odvození sdíleného tajemství a následně používá symetrické algoritmy pro vlastní šifrování dat a ochranu integrity. V rámci 3GPP je ECIES specifikováno jako kryptografická sada algoritmů pro určité ochranné mechanismy, zejména pro šifrování a ochranu integrity přenosových zpráv [NAS](/mobilnisite/slovnik/nas/) přenášejících data politik UE od funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) k UE.

Schéma funguje v několika odlišných fázích. Nejprve fáze generování klíče zahrnuje entitu (např. síťovou funkci), která vygeneruje pár klíčů eliptické křivky: soukromý klíč a odpovídající veřejný klíč. Proces šifrování, prováděný odesílatelem (např. PCF), zahrnuje generování efemérního páru klíčů eliptické křivky, použití veřejného klíče příjemce (UE) a vlastního efemérního soukromého klíče k výpočtu sdíleného tajemství pomocí Diffie-Hellmanova protokolu na eliptických křivkách (ECDH). Toto sdílené tajemství je následně zpracováno funkcí pro odvození klíče ([KDF](/mobilnisite/slovnik/kdf/)) za účelem vygenerování symetrických klíčů pro šifrování a generování kódu autentizace zprávy ([MAC](/mobilnisite/slovnik/mac/)). Samotný otevřený text je zašifrován pomocí symetrického šifrovacího algoritmu (jako je [AES](/mobilnisite/slovnik/aes/)). Nakonec je nad šifrovým textem a dalšími parametry vypočítán MAC. Přenášená zpráva se skládá z efemérního veřejného klíče, šifrového textu a MAC.

Na straně dešifrování použije příjemce (UE) svůj vlastní statický soukromý klíč a přijatý efemérní veřejný klíč k výpočtu stejného sdíleného tajemství, odvození stejných symetrických klíčů, ověření MAC a následnému dešifrování šifrového textu. Jeho role v síti 3GPP je vysoce specializovaná. Je primárně využíváno v jádru sítě 5G pro zabezpečené doručování politik UE ([URSP](/mobilnisite/slovnik/ursp/), ANDSP) z funkce řízení politik (PCF) k UE prostřednictvím funkce správy přístupu a mobility (AMF) za použití procedur přenosu NAS. Toto zajišťuje, že citlivá pravidla politik, která určují, jak má UE směrovat provoz, jsou doručena důvěrně a s integritou, což brání manipulaci nebo odposlechu.

## K čemu slouží

ECIES bylo přijato 3GPP, aby řešilo potřebu efektivního, standardizovaného šifrovacího schématu s veřejným klíčem vhodného pro prostředí s omezenými zdroji a specifické případy užití v rámci bezpečnostní architektury 5G. Primární problém, který řeší, je zabezpečené bod-bodové doručení citlivých konfiguračních dat (politik UE) ze sítě do zařízení. Předchozí metody mohly spoléhat na zabezpečení zavedené na nižších vrstvách (jako je šifrování AS a NAS) nebo jednodušší schémata, ale doručování řídicích politik vyžadovalo vyhrazený, koncový kryptografický ochranný mechanismus nezávislý na bezpečnostním kontextu přístupové vrstvy.

Motivace pro volbu ECIES oproti jiným schématům s veřejným klíčem, jako je RSA, spočívá ve výhodách kryptografie eliptických křivek (ECC). ECC poskytuje ekvivalentní úroveň zabezpečení jako RSA s výrazně menšími velikostmi klíčů (např. 256bitový klíč ECC nabízí zabezpečení srovnatelné s 3072bitovým klíčem RSA). To má za následek menší režii zpráv (menší veřejné klíče k přenosu), sníženou výpočetní zátěž (rychlejší operace) a nižší spotřebu energie – všechny tyto faktory jsou klíčové pro UE napájené baterií. Integrací dohody klíče, šifrování a MAC do jednoho standardizovaného schématu poskytuje ECIES kompaktní a kryptograficky robustní řešení. Jeho zavedení ve vydání 14 pro tento specifický účel zaplnilo mezeru v mechanismu poskytování politik a zajistilo, že řídicí příkazy řídicí roviny pocházející ze sítě, které přímo ovlivňují chování UE, jsou chráněny silnou, moderní kryptografií.

## Klíčové vlastnosti

- Hybridní šifrovací schéma kombinující ECC a symetrickou kryptografii
- Založeno na Diffie-Hellmanově protokolu na eliptických křivkách (ECDH) pro dohodu klíče
- Poskytuje důvěrnost (šifrování) i integritu (MAC)
- Používá efemérní klíče pro dopřednou důvěrnost (forward secrecy) v některých profilech
- Definováno jako kompletní sada algoritmů se specifikovanými funkcemi KDF, šifrování a MAC
- Nabízí vysoké zabezpečení s malými velikostmi klíčů, je efektivní pro implementaci v UE

## Související pojmy

- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [AES – Advanced Encryption Standard](/mobilnisite/slovnik/aes/)

## Definující specifikace

- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TR 33.841** (Rel-16) — Security aspects; Study on 256-bit algorithms for 5G
- **TS 33.885** (Rel-14) — Security Study for V2X Services
- **TR 33.938** (Rel-19) — 3GPP Cryptographic Inventory for 5G

---

📖 **Anglický originál a plná specifikace:** [ECIES na 3GPP Explorer](https://3gpp-explorer.com/glossary/ecies/)
