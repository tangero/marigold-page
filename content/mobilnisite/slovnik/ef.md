---
slug: "ef"
url: "/mobilnisite/slovnik/ef/"
type: "slovnik"
title: "EF – Elementary File"
date: 2025-01-01
abbr: "EF"
fullName: "Elementary File"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/ef/"
summary: "Elementární soubor (EF) je základní datová struktura uložená na UICC (Universal Integrated Circuit Card), která hostuje SIM aplikaci. Obsahuje specifické informace, jako jsou síťové autentizační klíče"
---

EF je základní datová struktura uložená na UICC (SIM kartě), která obsahuje specifické informace, jako jsou autentizační klíče, identita účastníka, položky telefonního seznamu a SMS, pro správu účastníka a přístup k síti.

## Popis

Elementární soubor (EF) je základní adresovatelný datový kontejner umístěný v rámci souborového systému UICC (Universal Integrated Circuit Card), který zahrnuje aplikace SIM, USIM a [ISIM](/mobilnisite/slovnik/isim/). Souborový systém UICC je hierarchicky organizován, počínaje Hlavním souborem ([MF](/mobilnisite/slovnik/mf/)) jako kořenem, pod kterým jsou Vyhrazené soubory ([DF](/mobilnisite/slovnik/df/)) představující aplikace (jako GSM nebo USIM aplikace), a uvnitř těchto DF se nacházejí Elementární soubory. Každý EF je identifikován jedinečným identifikátorem souboru ([FID](/mobilnisite/slovnik/fid/)) a lze jej vybrat pomocí standardních příkazů [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 7816-4. EF ukládají širokou škálu dat, strukturovaných buď jako transparentní (jednoduchá posloupnost bajtů), lineární s pevnou délkou (záznamy pevné délky), cyklické (pevný počet záznamů, kde je nejstarší přepsán) nebo [BER-TLV](/mobilnisite/slovnik/ber-tlv/) (datové objekty kódované ve formátu Tag-Length-Value).

Fungování EF je klíčové pro provoz UICC. Když mobilní zařízení ([ME](/mobilnisite/slovnik/me/)) potřebuje konkrétní data, například IMSI pro registraci v síti nebo autentizační klíč (Ki) pro bezpečnostní procedury, odešle příkaz (např. READ BINARY nebo READ RECORD) na UICC s uvedením FID cílového EF. Operační systém UICc soubor najde, provede případné kontroly přístupových podmínek (např. ověření PIN) a vrátí požadovaná data. Například EF_IMSI (identifikátor souboru '6F07') ukládá International Mobile Subscriber Identity. ME tento soubor čte během počáteční registrace, aby se identifikovalo vůči síti. Podobně EF_LOCI ukládá informace o poloze, které síť aktualizuje, aby umožnila efektivní paging.

Klíčovými součástmi konceptu EF jsou struktura souboru, přístupové podmínky a přidružená metadata definovaná v hlavičce EF. Hlavička specifikuje typ souboru, velikost, délku záznamu (je-li aplikovatelné) a přístupové podmínky (např. vždy povoleno, vyžadován PIN1, vyžadován ADM). EF tvoří páteř pro ukládání jak povinných síťových parametrů (jako EF_KC pro šifrovací klíč v GSM), tak volitelných uživatelských dat (jako EF_PBR pro reference telefonního seznamu). Jejich úlohou je poskytovat standardizovaný, bezpečný a trvalý mechanismus úložiště, který je nezávislý na mobilním zařízení, a umožňuje tak mobilitu účastníka a bezpečnou autentizaci napříč různými handsety a sítěmi.

## K čemu slouží

Elementární soubor existuje proto, aby poskytoval standardizovanou, bezpečnou a organizovanou metodu pro ukládání kritických dat účastníka a aplikací na čipové kartě používané v mobilní telekomunikaci (UICC). Řeší problém, jak trvale spravovat širokou škálu dat – od tajných kryptografických klíčů po veřejné položky telefonního seznamu – způsobem, který je přístupný pro mobilní zařízení, ale chráněný před neoprávněným přístupem. Motivací pro jeho vytvoření byla původní specifikace GSM SIM, která potřebovala model souborového systému odvozený z norem ISO pro čipové karty, aby nahradila jednoduché paměťové úložiště používané v dřívějších celulárních technologiích.

Historický kontext je takový, že před standardizovaným souborovým systémem UICc byla data účastníka a síťové parametry často ukládány proprietárními formáty v samotném mobilním zařízení, což bránilo interoperabilitě a mobilitě účastníka. Zavedení EF spolu s hierarchií DF/MF vytvořilo univerzální 'datovou skříň', kde každá informace měla známou, standardizovanou polohu a metodu přístupu. To umožnilo jakémukoli kompatibilnímu mobilnímu zařízení interagovat s jakoukoli kompatibilní SIM kartou, což byl základní kámen globálního úspěchu GSM. Odstranilo to omezení tím, že oddělilo identitu účastníka a servisní profil od handsetu, což umožnilo snadné výměny telefonů při zachování čísla a služeb, a vynucením bezpečnosti prostřednictvím přístupových podmínek na úrovni souboru, čímž chránilo citlivá data, jako jsou autentizační klíče.

## Klíčové vlastnosti

- Definován jedinečným 2bajtovým identifikátorem souboru (FID) a volitelným krátkým identifikátorem souboru
- Několik strukturních typů: Transparentní, Lineární s pevnou délkou, Lineární s proměnnou délkou, Cyklický, BER-TLV
- Ukládá kritická data: IMSI (EF_IMSI), autentizační klíče (EF_Ke/EF_Kc), telefonní seznam (EF_ADN/EF_PBR), SMS (EF_SMS)
- Vynucuje přístupové podmínky (např. ALW, CHV, ADM) pro bezpečnost
- Vybírán pomocí příkazu SELECT FILE s použitím FID nebo cesty
- Čtení/aktualizace pomocí příkazů READ/WRITE BINARY nebo READ/WRITE RECORD

## Definující specifikace

- **TS 21.111** (Rel-19) — USIM and UICC Requirements for 3G
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.022** (Rel-19) — ME Personalisation Features for GSM/3G
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TS 31.105** (Rel-19) — Slice Subscriber Identity Module (SSIM) Application
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification
- **TS 31.131** (Rel-19) — C Language Binding for (U)SIM API
- **TS 31.829** (Rel-13) — ISIM Conformance Requirements Technical Report
- **TR 31.900** (Rel-19) — 3GPP TS 31.900: Security Interworking Guidance
- **TS 34.131** (Rel-19) — SIM API C Language Test Specification
- **TS 34.229** (Rel-19) — IMS SIP/SDP UE Conformance Testing for 5GS

---

📖 **Anglický originál a plná specifikace:** [EF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ef/)
