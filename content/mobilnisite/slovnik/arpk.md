---
slug: "arpk"
url: "/mobilnisite/slovnik/arpk/"
type: "slovnik"
title: "ARPK – Administrator Root Public Key"
date: 2025-01-01
abbr: "ARPK"
fullName: "Administrator Root Public Key"
category: "Security"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/arpk/"
summary: "ARPK je kryptografický veřejný klíč používaný v obecné bootstrapové architektuře (GBA) standardu 3GPP k ověření identity a autorizaci správce funkce síťové aplikace (NAF). Umožňuje zabezpečené, automa"
---

ARPK (Administrator Root Public Key) je kořenový veřejný klíč správce používaný v architektuře GBA standardu 3GPP k ověření identity a autorizaci správce funkce síťové aplikace (NAF) pro zabezpečené, automatizované zřizování klíčů.

## Popis

Administrator Root Public Key (ARPK) je základním prvkem v rámci obecné bootstrapové architektury ([GBA](/mobilnisite/slovnik/gba/)) standardu 3GPP, konkrétně definovaným pro funkci GBA Push. Funguje v rámci bezpečnostního rámce pro síťové aplikace. Z architektonického hlediska je ARPK asociován se správcem funkce síťové aplikace ([NAF](/mobilnisite/slovnik/naf/)). NAF je entita na straně sítě, která poskytuje služby uživatelskému zařízení (UE) a vyžaduje autentizaci. ARPK není klíč používaný pro přímou autentizaci uživatele, ale pro ověření identity samotného správce NAF.

V praxi se ARPK používá k ověření digitálních podpisů vytvořených správcem NAF. Když správce NAF potřebuje provést privilegované operace, jako je spuštění procedury GBA Push pro zřízení klíčů pro konkrétní službu na UE, podepíše relevantní data (např. identifikátor klíče nebo služby) svým odpovídajícím soukromým klíčem. Síťová entita přijímající tento požadavek, typicky funkce bootstrapového serveru ([BSF](/mobilnisite/slovnik/bsf/)) nebo v některých push modelech samotné UE, použije předem zřízený ARPK k validaci podpisu. Toto ověření zajišťuje, že administrační příkaz pochází z důvěryhodného, autorizovaného zdroje.

Role ARPK spočívá ve vytvoření kořene důvěry pro administrativní akce v ekosystému GBA. Jedná se o statický nebo dlouhodobě platný klíč, který je zabezpečeně zřízen relevantním síťovým entitám mimo provozní pásmo, před uvedením do provozu. Tento mechanismus odděluje správu zabezpečení služeb od základní autentizace v mobilní síti ([AKA](/mobilnisite/slovnik/aka/)), což umožňuje flexibilní a bezpečné zpřístupnění služeb. Ověřením identity správce zabraňuje tomu, aby škodliví aktéři neoprávněně spouštěli operace zřizování nebo správy klíčů, čímž chrání integritu bezpečnostního rámce služeb.

## K čemu slouží

ARPK byl zaveden, aby řešil potřebu zabezpečené a autorizované správy aplikačně specifických bezpečnostních přihlašovacích údajů v sítích 3GPP, zejména pro služby využívající funkci [GBA](/mobilnisite/slovnik/gba/) Push. Před jeho specifikací byly mechanismy pro autorizaci administrativních akcí pro zasílání klíčů na uživatelská zařízení méně formalizované, potenciálně spoléhající na implicitní důvěru v síť nebo slabší bezpečnostní modely. To představovalo riziko, protože neoprávněné push příkazy mohly ohrozit zabezpečení služeb.

K jeho vytvoření vedla expanze mobilních služeb vyžadujících zabezpečené zřízení klíčů mimo provozní pásmo. Služby jako multimediální telefonie (MMTel), zabezpečené zasílání zpráv nebo IoT aplikace potřebovaly způsob, jak mohou správci sítě proaktivně zřizovat přihlašovací údaje bez iniciování uživatelem. ARPK poskytuje standardizovanou, kryptograficky silnou metodu pro ověření identity těchto administrativních spouštěčů. Řeší problém zajištění, že pouze legitimní správci sítě mohou nařídit síti vygenerovat a doručit službě specifické klíče na UE, čímž udržují řetězec důvěry od jádra sítě až po koncovou aplikaci.

Historicky, jak se sítě 3GPP vyvíjely pro podporu širší škály IP služeb (IMS, IoT), se framework GBA stal nezbytným pro opakované využití mobilní autentizace pro tyto služby. Funkce GBA Push a následně i ARPK zaplnily mezeru pro scénáře, kde musí bezpečnostní nastavení iniciovat síť, nikoli uživatel. Řeší omezení čistě uživatelem iniciovaného bootstrapování tím, že umožňuje zabezpečené zřizování služeb mezi stroji a iniciované serverem, což je zásadní pro automatizované a bezproblémové uživatelské zážitky se službami.

## Klíčové vlastnosti

- Poskytuje kryptografickou autentizaci pro správce NAF
- Umožňuje autorizaci pro zahájení procedury GBA Push
- Vytváří kořen důvěry pro operace správy klíčů správcem
- Používá ověření digitálního podpisu pro integritu příkazů
- Podporuje zabezpečené, sítí iniciované zřizování služebních klíčů
- Odděluje správu zabezpečení aplikací od procedur základní autentizace AKA

## Definující specifikace

- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification

---

📖 **Anglický originál a plná specifikace:** [ARPK na 3GPP Explorer](https://3gpp-explorer.com/glossary/arpk/)
