---
slug: "csr"
url: "/mobilnisite/slovnik/csr/"
type: "slovnik"
title: "CSR – Certificate Signing Request"
date: 2025-01-01
abbr: "CSR"
fullName: "Certificate Signing Request"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/csr/"
summary: "Certificate Signing Request (CSR) je standardizovaný formát zprávy používaný v sítích 3GPP k vyžádání digitálního certifikátu od certifikační autority (CA). Obsahuje veřejný klíč a identifikační údaje"
---

CSR je standardizovaný formát zprávy používaný k vyžádání digitálního certifikátu od certifikační autority, který obsahuje veřejný klíč a identitu žadatele pro bezpečné ověřování a šifrovanou komunikaci.

## Popis

Certificate Signing Request (CSR) je klíčovou součástí infrastruktury veřejných klíčů ([PKI](/mobilnisite/slovnik/pki/)) v sítích 3GPP, definovanou v několika bezpečnostních specifikacích. Jedná se o strukturovaný datový objekt, typicky kódovaný ve formátu [PKCS](/mobilnisite/slovnik/pkcs/)#10, který entita (jako síťová funkce, uživatelské zařízení nebo aplikační server) vygeneruje a odešle důvěryhodné certifikační autoritě ([CA](/mobilnisite/slovnik/ca/)) za účelem získání digitálního certifikátu. CSR obsahuje několik podstatných polí: rozlišující jméno subjektu ([DN](/mobilnisite/slovnik/dn/)) identifikující entitu (např. Common Name, Organization, Country), veřejný klíč entity (obvykle [RSA](/mobilnisite/slovnik/rsa/) nebo [ECC](/mobilnisite/slovnik/ecc/)) a volitelné atributy nebo rozšíření specifikující použití klíče, rozšířené použití klíče nebo alternativní jména subjektu. Entita také podepíše CSR svým odpovídajícím soukromým klíčem, čímž certifikační autoritě prokáže, že tento soukromý klíč vlastní.

Proces generování CSR začíná, když entita vytvoří pár veřejného a soukromého klíče. Entita následně sestaví datovou strukturu CSR včetně svých identifikačních údajů a veřejného klíče a vypočítá kryptografický hash (např. SHA-256) těchto dat. Tento hash je zašifrován soukromým klíčem entity a vytvoří tak digitální podpis, který je připojen k CSR. Tento podpis umožňuje certifikační autoritě ověřit, že žadatel skutečně ovládá soukromý klíč odpovídající předloženému veřejnému klíči, a zabránit tak útokům vydávání se za jiného. CSR je přenášena k certifikační autoritě prostřednictvím zabezpečeného registračního protokolu, jako je Certificate Management Protocol ([CMP](/mobilnisite/slovnik/cmp/)) nebo Simple Certificate Enrollment Protocol (SCEP), často přes připojení chráněná protokolem [TLS](/mobilnisite/slovnik/tls/).

Po přijetí CSR certifikační autorita provede validační kontroly, včetně ověření podpisu CSR, autentizace identity žadatele prostřednictvím mimopásmových metod nebo existujících přihlašovacích údajů a zajištění souladu žádosti s certifikační politikou autority. Pokud validace uspěje, certifikační autorita vydá digitální certifikát podepsáním nové datové struktury obsahující veřejný klíč a identifikační údaje žadatele svým soukromým klíčem. Tento certifikát propojuje veřejný klíč s identitou a vytváří důvěryhodný přihlašovací údaj, který ostatní entity mohou ověřit pomocí veřejného klíče certifikační autority. V architekturách 3GPP se CSR používají pro zřizování certifikátů pro síťové funkce v architekturách založených na službách (SBA), což umožňuje vzájemné ověřování TLS mezi instancemi síťových funkcí, stejně jako pro certifikáty zařízení ve scénářích IoT a ověřování uživatelských zařízení.

Role CSR v zabezpečení 3GPP je mnohostranná. Umožňuje automatizovanou správu životního cyklu certifikátů a podporuje škálovatelné nasazení certifikátů napříč obrovským počtem síťových prvků a zařízení. V jádrových sítích 5G jsou CSR nedílnou součástí systému správy bezpečnostních přihlašovacích údajů pro ověřování síťových funkcí, což zajišťuje zabezpečená rozhraní založená na službách. Specifikace podrobně popisují formáty CSR, požadavky na zpracování a integraci s certifikačními registračními protokoly za účelem zachování interoperability mezi různými výrobci a operátory. Správné zacházení s CSR je nezbytné pro udržení řetězce důvěry, zabránění neoprávněnému vydávání certifikátů a zajištění celkové integrity ověřovacího rámce sítě.

## K čemu slouží

Certificate Signing Request slouží k poskytnutí standardizovaného, bezpečného mechanismu, pomocí kterého mohou entity v sítích 3GPP žádat o digitální certifikáty od důvěryhodných autorit. Řeší základní problém bezpečného propojení veřejných klíčů s identitami škálovatelným a automatizovaným způsobem, což je zásadní pro ověřování, důvěrnost a integritu v moderních telekomunikačních systémech. Bez CSR by zřizování certifikátů vyžadovalo manuální procesy náchylné k chybám, nekonzistenci a bezpečnostním slabinám, což by znemožnilo rozsáhlé nasazení.

Historicky se dřívější generace mobilních sítí spoléhaly na jednodušší systémy s předem sdílenými klíči nebo proprietární metody ověřování, kterým chyběla flexibilita a škálovatelnost vyžadovaná pro dynamickou architekturu 5G založenou na službách. Přechod na cloud-nativní, softwarově definované sítě s množstvím propojených síťových funkcí vytvořil potřebu automatizovaného vzájemného ověřování založeného na certifikátech. CSR poskytuje základní žádostní mechanismus, který tuto automatizaci umožňuje, a dává síťovým funkcím, zařízením a aplikacím možnost získat přihlašovací údaje bez manuálního zásahu. Tím se řeší omezení předchozích přístupů, které nedokázaly podpořit rychlé škálování, zřizování bez zásahu obsluhy a dynamické vztahy důvěry vyžadované v 5G a dalších generacích.

Vytvoření specifikací CSR v rámci 3GPP bylo motivováno potřebou interoperabilního zabezpečení napříč nasazeními více výrobců a požadavkem na integraci s existujícími ekosystémy PKI. Standardizací formátů a zpracování CSR 3GPP zajišťuje, že různé síťové prvky od různých výrobců mohou bezpečně získávat certifikáty od operátorských nebo třetích certifikačních autorit, a tím udržovat konzistentní bezpečnostní politiky v celé síti. To umožňuje funkce jako zabezpečená rozhraní založená na službách, ověřování zařízení IoT a zabezpečení síťového řezání, kde různé řezy mohou vyžadovat odlišné certifikační autority a modely důvěry.

## Klíčové vlastnosti

- Standardizovaný formát PKCS#10 pro interoperabilitu napříč výrobci a systémy
- Obsahuje identifikační údaje subjektu a veřejný klíč pro propojení v certifikátu
- Digitálně podepsán žadatelem k prokázání vlastnictví soukromého klíče
- Podporuje rozšíření pro politiky použití klíče a alternativní jména subjektu
- Umožňuje automatizovanou registraci certifikátů prostřednictvím protokolů jako CMP a SCEP
- Integruje se s bezpečnostní architekturou 3GPP pro ověřování síťových funkcí

## Definující specifikace

- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.794** (Rel-19) — Study on Zero Trust Security Enablers for 5G
- **TR 33.876** (Rel-18) — Technical Report on Certificate Management

---

📖 **Anglický originál a plná specifikace:** [CSR na 3GPP Explorer](https://3gpp-explorer.com/glossary/csr/)
