---
slug: "multos"
url: "/mobilnisite/slovnik/multos/"
type: "slovnik"
title: "MULTOS – Multi-application Operating System"
date: 2025-01-01
abbr: "MULTOS"
fullName: "Multi-application Operating System"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/multos/"
summary: "MULTOS je víceaplikací operační systém pro čipové karty standardizovaný 3GPP pro prostředí bezpečnostních prvků. Umožňuje bezpečný běh více aplikací na jediném čipu a podporuje vlastnosti jako odolnos"
---

MULTOS je víceaplikací operační systém pro čipové karty standardizovaný 3GPP pro bezpečnostní prvky, který umožňuje bezpečný běh více aplikací na jediném čipu s vlastnostmi jako je odolnost proti narušení a dynamická správa.

## Popis

MULTOS (Multi-application Operating System) je vysoce zabezpečený operační systém pro čipové karty odkazovaný ve specifikacích 3GPP pro použití v telekomunikacích, zejména v [SIM](/mobilnisite/slovnik/sim/) kartách a bezpečnostních prvcích. Je navržen jako víceaplikací platforma, která umožňuje koexistenci více nezávislých aplikací na jediném čipu čipové karty při zachování silných bezpečnostních hranic. Architektura MULTOS je založena na vrstveném modelu, který zahrnuje vrstvu abstrakce hardwaru, jádro a aplikační vrstvu. Jádro poskytuje základní služby jako správa paměti, kryptografické funkce a správa životního cyklu aplikací. Každá aplikace běží ve vlastním izolovaném prostředí, což zabraňuje neoprávněnému přístupu nebo vzájemnému ovlivňování aplikací, což je klíčové pro ochranu citlivých dat, jako jsou autentizační klíče a uživatelské přihlašovací údaje.

Fungování MULTOS zahrnuje důsledný proces certifikace a načítání. Aplikace musí být před instalací na kartu digitálně podepsány důvěryhodnou certifikační autoritou. Operační systém tyto podpisy při instalaci ověřuje, čímž zajišťuje běh pouze autorizovaného kódu. MULTOS podporuje dynamickou správu aplikací, což znamená, že aplikace lze přidávat, aktualizovat nebo mazat po vydání karty bez narušení bezpečnosti ostatních aplikací nebo samotného OS. Mezi klíčové komponenty patří MULTOS Execution Environment (MEXE), který zajišťuje provádění aplikací, a Security Domain Manager, který vynucuje politiky řízení přístupu. Kryptografické schopnosti jsou vestavěné a podporují algoritmy jako [AES](/mobilnisite/slovnik/aes/), [RSA](/mobilnisite/slovnik/rsa/) a [ECC](/mobilnisite/slovnik/ecc/) pro šifrování, dešifrování a digitální podpisy.

V kontextu sítí 3GPP je MULTOS specifikován pro implementace UICC (Universal Integrated Circuit Card) a eSIM (embedded SIM). Hraje zásadní roli při zabezpečení identity účastníka a umožňuje funkce jako over-the-air ([OTA](/mobilnisite/slovnik/ota/)) provizionování a podpora více operátorů. Odolný design operačního systému proti narušení chrání před fyzickými a logickými útoky, což jej činí vhodným pro zařízení IoT, mobilní platby a správu identit. Poskytnutím standardizované, bezpečné platformy MULTOS zajišťuje interoperabilitu mezi různými výrobci karet a síťovými operátory a podporuje důvěru v mobilní a IoT ekosystémy.

## K čemu slouží

MULTOS byl zaveden ve 3GPP Release 12, aby řešil potřebu bezpečného, víceaplikací operačního systému pro čipové karty v rozvíjejících se telekomunikačních prostředích. Před jeho přijetím byly operační systémy čipových karet často proprietární nebo omezené na jedinou aplikaci, což omezovalo flexibilitu a bezpečnost pro nové služby, jako je mobilní bankovnictví, autentizace IoT a [SIM](/mobilnisite/slovnik/sim/) karty pro více operátorů. Růst připojených zařízení a digitálních služeb vyžadoval platformu, která by mohla bezpečně hostovat více aplikací na jediném čipu, snižovat náklady a složitost a zároveň zvyšovat bezpečnost.

Vznik MULTOS byl motivován omezeními předchozích OS pro čipové karty, kterým chyběla robustní izolace aplikací a schopnosti dynamické správy. Historické přístupy riskovaly narušení bezpečnosti, pokud se aplikace vzájemně ovlivňovaly nebo pokud byl načten neautorizovaný kód. MULTOS tyto problémy řeší tím, že poskytuje certifikované, standardizované prostředí se silnými kryptografickými základy a odolností proti narušení. Umožňuje síťovým operátorům a poskytovatelům služeb nasazovat nové aplikace over-the-air, čímž podporuje inovace v mobilních službách a IoT bez nutnosti fyzické výměny karty. Tím řeší potřebu škálovatelného, budoucím výzvám odolného zabezpečení ve stále více propojeném světě.

## Klíčové vlastnosti

- Podpora více aplikací se silnou izolací mezi aplikacemi
- Dynamická správa aplikací (načítání, aktualizace, mazání po vydání)
- Odolný design hardwaru a softwaru proti narušení
- Vestavěné kryptografické funkce (např. AES, RSA, ECC)
- Certifikace a ověřování digitálních podpisů pro zabezpečení aplikací
- Standardizováno v 3GPP pro implementace UICC a eSIM

## Definující specifikace

- **TR 35.934** (Rel-19) — Tuak algorithm set for 3GPP auth & key gen

---

📖 **Anglický originál a plná specifikace:** [MULTOS na 3GPP Explorer](https://3gpp-explorer.com/glossary/multos/)
