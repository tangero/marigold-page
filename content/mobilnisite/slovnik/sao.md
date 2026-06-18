---
slug: "sao"
url: "/mobilnisite/slovnik/sao/"
type: "slovnik"
title: "SAO – Single Association Object"
date: 2025-01-01
abbr: "SAO"
fullName: "Single Association Object"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sao/"
summary: "Datová jednotka používaná v protokolu Diameter pro rozhraní 3GPP. Zapouzdřuje jeden příkaz Diameter a s ním spojené páry atribut-hodnota (AVP) pro spolehlivý přenos a zpracování mezi síťovými funkcemi"
---

SAO je datová jednotka protokolu Diameter, která zapouzdřuje jeden příkaz a jeho atributy AVP pro přenos mezi síťovými funkcemi, jako jsou PCRF a AF.

## Popis

Objekt s jedním sdružením (Single Association Object, SAO) je základní konstrukcí v rámci protokolového rámce Diameter podle 3GPP, konkrétně definovanou pro referenční body Rx a Gx. Slouží jako standardizovaný kontejner neboli datová jednotka protokolu ([PDU](/mobilnisite/slovnik/pdu/)) pro přenos kompletní transakce Diameter. SAO zapouzdřuje právě jeden příkaz (neboli zprávu) Diameter spolu se všemi jeho povinnými a volitelnými páry atribut-hodnota ([AVP](/mobilnisite/slovnik/avp/)). Toto zapouzdření poskytuje jasně definovanou strukturu, která zajišťuje interoperabilitu mezi různými implementacemi síťových funkcí od různých dodavatelů, jako je funkce pravidel pro účtování a zásad ([PCRF](/mobilnisite/slovnik/pcrf/)), aplikační funkce ([AF](/mobilnisite/slovnik/af/)) a funkce vynucování pravidel pro účtování a zásad ([PCEF](/mobilnisite/slovnik/pcef/)).

Fungování SAO je vnitřně propojeno se základním protokolem Diameter ([RFC](/mobilnisite/slovnik/rfc/) 6733). Když entita aplikační vrstvy, například AF potřebující signalizovat informace o službě, vygeneruje požadavek Diameter (např. AA-Request), vytvoří zprávu s příslušným kódem příkazu a AVP. Tato kompletní zpráva je poté naformátována jako SAO pro přenos přes rozhraní Rx. Přijímající protějšek Diameter, typicky PCRF, SAO dekóduje, ověří jeho strukturu a obsah podle specifikací 3GPP a zpracuje obsažený příkaz. Odpovídající odpověď (např. AA-Answer) je také odeslána zpět jako SAO.

Klíčové součásti konceptu SAO zahrnují hlavičku Diameter, která obsahuje kód příkazu a příznaky, a sekvenci AVP, které nesou skutečné informace o relaci a zásadách, jako je Subscription-Id, Media-Component-Description nebo QoS-Information. Úlohou SAO je být atomickou jednotkou výměny pro signalizaci řízení zásad a účtování. Jeho standardizovaný formát zaručuje, že složité zprávy s více AVP jsou konzistentně serializovány a deserializovány v síti, což umožňuje přesnou kontrolu nad QoS na úrovni přenosu, řízením přístupu a pravidly účtování na základě požadavků relace aplikační vrstvy.

## K čemu slouží

SAO bylo vytvořeno za účelem poskytnutí robustního, jednoznačného a standardizovaného kontejneru pro zprávy pro architekturu řízení zásad a účtování ([PCC](/mobilnisite/slovnik/pcc/)) založenou na protokolu Diameter, zavedenou ve vydání 3GPP Release 7. Před PCC byly mechanismy řízení zásad roztříštěnější a méně dynamické. Zavedení rozhraní Rx a Gx vyžadovalo spolehlivou metodu pro komunikaci podrobností relace od aplikačních funkcí (jako je [P-CSCF](/mobilnisite/slovnik/p-cscf/) pro IMS) k centralizovanému bodu pro rozhodování o zásadách (PCRF).

SAO řeší problém nekonzistentního formátování a parsování zpráv mezi síťovými prvky od různých výrobců. Definováním jediného, atomického objektu, který obsahuje kompletní transakci Diameter, zajistilo 3GPP, že všechny implementace budou zacházet se zprávami shodně, od kódování AVP na úrovni bajtů až po řazení příkazů. Tato interoperabilita byla klíčová pro komerční nasazení IMS a dalších pokročilých služeb závislých na dynamickém řízení zásad.

Historicky vycházela motivace z potřeby posunu za statické, předem nakonfigurované QoS směrem k dynamickým zásadám uvědomujícím si relaci. SAO jako nosič těchto dynamických parametrů relace umožnilo PCRF činit informovaná rozhodnutí v reálném čase. Odstranilo omezení dřívějších přístupů tím, že poskytlo formalizovanou strukturu vyžadovanou specifikací, která snížila chyby integrace a urychlila nasazení kombinovaných funkcí zásad a účtování v mobilních širokopásmových sítích.

## Klíčové vlastnosti

- Zapouzdřuje jeden kompletní příkaz Diameter a s ním spojená AVP.
- Standardizovaný formát pro referenční body Rx (AF-PCRF) a Gx (PCRF-PCEF).
- Zajišťuje interoperabilitu mezi síťovými funkcemi řízení zásad a účtování (PCC) od více dodavatelů.
- Podporuje přenos složitých parametrů relace pro dynamická rozhodnutí o zásadách.
- Usnadňuje spolehlivé a jednoznačné parsování zpráv Diameter přijímajícími entitami.
- Slouží jako atomická datová jednotka protokolu (PDU) pro signalizaci Diameter související s PCC.

## Definující specifikace

- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification

---

📖 **Anglický originál a plná specifikace:** [SAO na 3GPP Explorer](https://3gpp-explorer.com/glossary/sao/)
