---
slug: "gsid"
url: "/mobilnisite/slovnik/gsid/"
type: "slovnik"
title: "GSID – GAA Service Identifier"
date: 2025-01-01
abbr: "GSID"
fullName: "GAA Service Identifier"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/gsid/"
summary: "GAA Service Identifier (GSID) je jedinečný identifikátor používaný v rámci architektury GAA (Generic Authentication Architecture). Identifikuje konkrétní službu nebo aplikaci, která využívá GAA pro na"
---

GSID je jedinečný identifikátor v rámci architektury GAA (Generic Authentication Architecture), který identifikuje konkrétní službu využívající GAA pro navázání zabezpečeného přístupu.

## Popis

[GAA](/mobilnisite/slovnik/gaa/) Service Identifier (GSID) je klíčová součást architektury GAA (Generic Authentication Architecture) standardizované 3GPP, specifikovaná v dokumentech jako TS 29.109 a TS 33.980. GAA poskytuje obecný mechanismus pro využití silné autentizace UICC (Universal Integrated Circuit Card, např. SIM karty) v uživatelském zařízení k zabezpečení aplikací a služeb mimo základní mobilní síť, jako je multimediální vysílání ([MBMS](/mobilnisite/slovnik/mbms/)), zabezpečení uživatelské roviny nebo služby třetích stran. GSID jednoznačně identifikuje poskytovatele služby nebo konkrétní aplikaci, která žádá o autentizační přihlašovací údaje od infrastruktury GAA.

Operačně, když se aplikace na uživatelském zařízení (UE) potřebuje autentizovat u služby (Network Application Function, [NAF](/mobilnisite/slovnik/naf/)), kontaktuje funkci [BSF](/mobilnisite/slovnik/bsf/) (Bootstrapping Server Function). BSF provede s UE a jeho domácím účastnickým systémem ([HSS](/mobilnisite/slovnik/hss/)) bootstrapovací proceduru k vytvoření sdíleného dočasného tajného klíče. UE a BSF z tohoto bootstrapovaného klíče odvodí klíče specifické pro danou aplikaci. GSID je klíčový parametr v tomto procesu odvozování klíčů. Je součástí autentizační výměny mezi UE a BSF a následně mezi UE a NAF. Použití GSID zajišťuje, že odvozené klíče jsou jedinečné pro danou konkrétní službu, což poskytuje kryptografickou separaci. To znamená, že klíč odvozený pro jednu službu (identifikovanou jedním GSID) nelze použít k napodobení nebo přístupu k jiné službě (s jiným GSID).

Z architektonického hlediska je GSID součástí kontextových informací služby. BSF poskytuje GSID NAF a UE nezávisle zná GSID pro službu, ke které přistupuje (často je nakonfigurován v aplikaci). NAF používá GSID spolu s dalšími identifikátory, jako je Bootstrapping Transaction Identifier ([B-TID](/mobilnisite/slovnik/b-tid/)), k vyžádání odpovídajícího klíčového materiálu od BSF. Tato architektura umožňuje, aby jedna bootstrapovací událost podpořila zabezpečený přístup k více službám, z nichž každá je identifikována vlastním GSID, aniž by uživatel musel zadávat hesla. GSID tedy funguje jako jmenný prostor v ekosystému GAA a umožňuje škálovatelnou, zabezpečenou a na službu specifickou autentizaci odvozenou z robustní 3GPP účastnické autentizace.

## K čemu slouží

GSID byl vytvořen k řešení problému zabezpečené a pohodlné autentizace pro přidané služby bez rozšiřování uživatelských přihlašovacích údajů. Před [GAA](/mobilnisite/slovnik/gaa/) a identifikátory jako GSID museli poskytovatelé služeb (např. pro vysílání TV, bankovní aplikace nebo firemní přístup) implementovat vlastní autentizační systémy, které se často spoléhaly na slabé kombinace uživatelského jména a hesla nebo složitá nasazení infrastruktury veřejných klíčů (PKI), která byla pro uživatele těžkopádná. Architektura GAA od 3GPP si kladla za cíl znovu využít silnou a všudypřítomnou autentizaci již přítomnou na SIM kartě.

GSID je pro tento model zásadní, protože poskytuje diferenciaci služeb. Bez jedinečného identifikátoru služby by mohl být jediný bootstrapovaný bezpečnostní kontext zneužit k přístupu k jakékoli službě využívající GAA, což by představovalo významné bezpečnostní riziko. GSID zajišťuje, že kryptografický materiál vygenerovaný během bootstrapování je pevně vázán na konkrétního poskytovatele služeb a aplikaci. Tím se řeší omezení univerzálního klíče a umožňuje se „obecný“ aspekt GAA – podpora více nezávislých služeb z jediného autentizačního bootstrapu. Jeho zavedení v Release 8 spolu s širším rámcem GAA umožnilo mobilním operátorům bezpečně nabízet platformu pro služby třetích stran, což podpořilo inovace při zachování vysokých bezpečnostních standardů odvozených z mobilní sítě.

## Klíčové vlastnosti

- Jednoznačně identifikuje službu nebo aplikaci v rámci architektury GAA
- Používá se jako vstup do funkce pro odvozování klíčů k vygenerování klíčů specifických pro službu
- Zajišťuje kryptografickou separaci mezi různými službami využívajícími GAA
- Přenáší se mezi UE, BSF a NAF během autentizačních procedur
- Umožňuje, aby jedna bootstrapovací relace podpořila více služeb
- Základní prvek pro obecnou a škálovatelnou povahu architektury GAA

## Související pojmy

- [BSF – Bootstrapping Server Function](/mobilnisite/slovnik/bsf/)
- [NAF – Network Application Function](/mobilnisite/slovnik/naf/)

## Definující specifikace

- **TS 29.109** (Rel-19) — GAA Bootstrapping Interfaces (Zh, Dz, Zn, Zpn)
- **TR 33.980** (Rel-19) — GAA & Liberty Alliance Interworking Guidelines

---

📖 **Anglický originál a plná specifikace:** [GSID na 3GPP Explorer](https://3gpp-explorer.com/glossary/gsid/)
