---
slug: "fcp"
url: "/mobilnisite/slovnik/fcp/"
type: "slovnik"
title: "FCP – File Control Parameters"
date: 2025-01-01
abbr: "FCP"
fullName: "File Control Parameters"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fcp/"
summary: "Parametry řízení souborů (File Control Parameters) jsou souborem datových prvků definovaných v rámci aplikační sady nástrojů USIM pro správu operací se soubory na UICC. Určují přístupové podmínky, str"
---

FCP je soubor datových prvků v sadě nástrojů USIM, které definují přístupové podmínky, strukturu a zabezpečení pro soubory na UICC za účelem zajištění bezpečného a organizovaného ukládání dat.

## Popis

Parametry řízení souborů (File Control Parameters) jsou klíčovou součástí architektury UICC (Universal Integrated Circuit Card) a USIM (Universal Subscriber Identity Module), definovanou v rámci aplikační sady nástrojů USIM (USAT). Jedná se o metadata spojená s každým souborem (jak základními soubory, EFs, tak vyhrazenými soubory, DFs) v souborovém systému UICC. Tyto parametry jsou uloženy v hlavičce souboru nebo ve vyhrazeném administrativním souboru a jsou čteny terminálem (mobilním zařízením), aby správně a bezpečně porozuměl interakci s konkrétním souborem. Parametry definují základní charakteristiky souboru a pravidla pro přístup k jeho obsahu.

Struktura a kódování FCP jsou standardizovány, primárně v dokumentu 3GPP TS 31.102, který podrobně popisuje charakteristiky USIM. Když terminál vybere soubor na UICC, obdrží v odpovědi parametry řízení souborů. Tyto parametry zahrnují velikost souboru (udávající počet bajtů), identifikátor souboru (jedinečnou 2bajtovou adresu), stav životního cyklu souboru (např. vytvořený, inicializovaný, provozní, ukončený) a především bezpečnostní atributy. Bezpečnostní atributy definují přístupové podmínky pro různé operace, jako je čtení, aktualizace, zvýšení hodnoty nebo zneplatnění souboru. Tyto podmínky mohou být 'vždy', 'nikdy' nebo mohou vyžadovat specifický bezpečnostní kontext, jako je úspěšné ověření PINu ([CHV](/mobilnisite/slovnik/chv/)), administrativní klíče ([ADM](/mobilnisite/slovnik/adm/)), nebo může být přístup nikdy nepovolen.

Dále mohou FCP určovat strukturu souboru, například zda se jedná o soubor lineární s pevnou strukturou, lineární s proměnnou strukturou, cyklický nebo transparentní. Pro strukturované soubory jsou zahrnuty další parametry, jako je délka záznamu nebo počet záznamů. Role FCP je zásadní; fungují jako soubor pravidel, který řídí všechny interakce se souborovým systémem na čipové kartě. Bez správné interpretace FCP by terminál nemohl číst identitu účastníka ([IMSI](/mobilnisite/slovnik/imsi/)), síťové autentizační klíče (Ki), položky telefonního seznamu ani úložiště SMS. Vynucují bezpečnostní model, čímž zabraňují neoprávněnému přístupu k citlivým datům a zajišťují integritu souborového systému UICC, který představuje důvěryhodné prostředí v ekosystému mobilní sítě.

## K čemu slouží

Účelem parametrů řízení souborů je poskytnout standardizovaný, bezpečný a flexibilní mechanismus pro správu hierarchického souborového systému na čipové kartě UICC. Před takovou standardizací vedly proprietární metody správy souborů k problémům s interoperabilitou mezi různými výrobci karet a mobilních zařízení. Rámec FCP tento problém řeší definicí univerzální sady metadat, kterou může interpretovat jakýkoli kompatibilní terminál, což umožňuje bezproblémovou interakci s USIM od jakéhokoli dodavatele.

Jejich vytvoření bylo motivováno potřebou robustního modelu zabezpečení a řízení přístupu na modulu identity účastníka. Karta SIM/USIM ukládá vysoce citlivé informace, včetně jedinečné identity účastníka ([IMSI](/mobilnisite/slovnik/imsi/)), dlouhodobého autentizačního klíče (Ki) a osobních dat. FCP vynucují povinné řízení přístupu a zajišťují, že ke kritickým souborům nelze přistupovat pro čtení nebo úpravy bez řádného ověření (např. ověření PINu). Tím chrání účastníka před krádeží identity a síť před podvodným přístupem. Navíc, jak se USIM vyvinul z jednoduchého autentizačního tokenu na platformu pro více aplikací (USAT), systém FCP poskytl potřebnou strukturu pro správu komplexního, víceaplikačního souborového systému s různými bezpečnostními požadavky pro různé soubory a aplikace.

## Klíčové vlastnosti

- Definuje povinné přístupové podmínky pro operace se soubory (READ, UPDATE, INVALIDATE, REHABILITATE).
- Určuje typ struktury souboru (transparentní, lineární s pevnou strukturou, cyklický atd.) a související parametry velikosti.
- Udává stav životního cyklu souboru (např. vytvořený, inicializovaný, provozní).
- Obsahuje jedinečný identifikátor souboru používaný pro příkazy výběru souboru.
- Může zahrnovat bezpečnostní atributy odkazující na konkrétní PINy nebo administrativní klíče.
- Poskytuje standardizovanou šablonu (kódovanou BER-TLV) pro interoperabilní správu souborů.

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.102** (Rel-19) — USIM Application Specification

---

📖 **Anglický originál a plná specifikace:** [FCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/fcp/)
