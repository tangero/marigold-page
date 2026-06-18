---
slug: "saa"
url: "/mobilnisite/slovnik/saa/"
type: "slovnik"
title: "SAA – Server Assignment Answer"
date: 2025-01-01
abbr: "SAA"
fullName: "Server Assignment Answer"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/saa/"
summary: "Zpráva protokolu Diameter používaná v rozhraní Cx v rámci IMS. Je odesílána Home Subscriber Server (HSS) směrem k Interrogating-Call Session Control Function (I-CSCF) jako odpověď na Server Assignment"
---

SAA je zpráva protokolu Diameter odesílaná HSS směrem k I-CSCF jako odpověď na Server Assignment Request, která v rámci rozhraní IMS Cx poskytuje data pro autentizaci uživatele a jeho služební profil.

## Popis

Server Assignment Answer (SAA) je klíčový příkaz protokolu Diameter v architektuře 3GPP IP Multimedia Subsystem (IMS). Je definován ve specifikaci rozhraní Cx (TS 23.380 a související) jako odpověď na zprávu Server Assignment Request ([SAR](/mobilnisite/slovnik/sar/)). SAA je odesílána z Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), centrální databáze uživatelů, směrem k Interrogating-Call Session Control Function ([I-CSCF](/mobilnisite/slovnik/i-cscf/)). Tato výměna probíhá během klíčových procedur registrace a navazování relace v IMS za účelem autorizace uživatele a získání jeho služební konfigurace.

Když se User Equipment (UE) pokouší zaregistrovat v IMS síti, [I-CSCF](/mobilnisite/slovnik/icscf/) přijme požadavek [SIP](/mobilnisite/slovnik/sip/) REGISTER. I-CSCF poté odešle HSS zprávu Diameter SAR k provedení přiřazení serveru. SAR informuje HSS o tom, který Serving-CSCF ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) byl vybrán nebo je dotazován pro obsluhu uživatele. HSS tento požadavek zpracuje, což zahrnuje kontrolu stavu uživatelského předplatného, autentizačních dat a schopností nominovaného S-CSCF. HSS následně sestaví a odešle SAA zpět k I-CSCF. Zpráva SAA přenáší několik klíčových atributů ([AVP](/mobilnisite/slovnik/avp/)), především autentizační vektory uživatele (pro SIP digest autentizaci), jméno přiřazeného S-CSCF v případě úspěšné registrace a IMS služební profil uživatele. Služební profil obsahuje initial Filter Criteria (iFC), což jsou spouštěče určující, jak mají být příchozí SIP zprávy pro daného uživatele směrovány ke konkrétním Application Server ([AS](/mobilnisite/slovnik/as/)).

Obsah zprávy SAA přímo určuje následné akce I-CSCF. Pokud SAA obsahuje úspěšný výsledný kód a jméno S-CSCF, I-CSCF přepošle požadavek SIP REGISTER tomuto konkrétnímu S-CSCF. Autentizační vektory obsažené v SAA používá S-CSCF k výzvě směrem k UE. Pokud HSS přiřazení odmítne (např. uživatel neznámý nebo zablokovaný), SAA bude obsahovat příslušný chybový kód a I-CSCF pokus o registraci ukončí a odešle SIP chybovou odpověď směrem k UE. SAA je tedy autoritativní odpověď, která řídí přístup k IMS službám a propojuje data o účastníkovi v HSS s dynamickou logikou řízení relací v CSCFs.

## K čemu slouží

Zpráva SAA existuje jako součást rozhraní Cx založeného na protokolu Diameter za účelem oddělení správy dat účastníka od řízení relací v IMS. V architekturách před IMS byla uživatelská data a logika řízení hovorů často těsně integrována, což činilo sítě nepružnými a obtížně škálovatelnými. Model IMS zavedl jasné oddělení: HSS uchovává všechna data o předplatném a autentizaci, zatímco CSCFs zpracovávají signalizaci relací. Transakce SAR/SAA je protokolový mechanismus, který toto oddělení propojuje.

Tento návrh řeší několik klíčových problémů. Za prvé umožňuje centralizovanou správu účastníků. Jediný HSS může obsluhovat více CSCFs a další síťové funkce, což zajišťuje konzistenci. Za druhé umožňuje dynamické přiřazení S-CSCF. I-CSCF může dotazovat HSS (prostřednictvím SAR) na vhodný S-CSCF na základě uživatelských schopností a HSS odpoví (prostřednictvím SAA) přiřazením, což umožňuje vyrovnávání zátěže a směrování založené na službách. Za třetí poskytuje zabezpečenou a standardizovanou metodu pro distribuci citlivých autentizačních dat z HSS na okraj sítě (k S-CSCF) pouze v případě potřeby, podle modelu požadavek-odpověď. SAA, jakožto zabezpečený kontejner pro tato data, je zásadní pro autentizaci a autorizaci v IMS.

## Klíčové vlastnosti

- Příkaz odpovědi protokolu Diameter v rozhraní Cx (kód 3001)
- Přenáší autentizační vektory uživatele (RAND, AUTN, XRES, IK, CK)
- Poskytuje jméno/adresu přiřazeného Serving-CSCF (S-CSCF)
- Přenáší IMS služební profil uživatele a initial Filter Criteria (iFC)
- Předává výsledek operace přiřazení serveru (úspěch nebo chyba)
- Podporuje více stavů registrace (např. registrace, opětovná registrace, zrušení registrace)

## Související pojmy

- [SAR – Security Assurance Requirements](/mobilnisite/slovnik/sar/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [I-CSCF – Interrogating-Call Session Control Function](/mobilnisite/slovnik/i-cscf/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.380** (Rel-19) — IMS Restoration Procedures

---

📖 **Anglický originál a plná specifikace:** [SAA na 3GPP Explorer](https://3gpp-explorer.com/glossary/saa/)
