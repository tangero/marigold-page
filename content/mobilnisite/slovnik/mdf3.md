---
slug: "mdf3"
url: "/mobilnisite/slovnik/mdf3/"
type: "slovnik"
title: "MDF3 – Mediation and Delivery Function 3"
date: 2025-01-01
abbr: "MDF3"
fullName: "Mediation and Delivery Function 3"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mdf3/"
summary: "Bezpečnostní funkce pro zákonný odposlech a uchovávání dat. Zprostředkovává a doručuje událostmi řízená data a archivované záznamy o archivovaných datech orgánům činným v trestním řízení nebo jiným op"
---

MDF3 je bezpečnostní funkce 3GPP, která zprostředkovává a doručuje událostmi řízená data a archivované záznamy oprávněným subjektům pro účely zákonného odposlechu a forenzní analýzy.

## Popis

Funkce zprostředkování a doručení 3 (MDF3) je specializovaná bezpečnostní funkce v rámci architektury 3GPP, definovaná společně s [MDF2](/mobilnisite/slovnik/mdf2/) pro zákonný odposlech ([LI](/mobilnisite/slovnik/li/)) a uchovávání dat ([DR](/mobilnisite/slovnik/dr/)). Zatímco MDF2 zpracovává obsah komunikace a informace související s odposlechem v reálném nebo téměř reálném čase, MDF3 je konkrétně určena ke zprostředkování a doručování archivovaných dat a záznamů o událostech. To zahrnuje data, která jsou provozovatelé sítí zákonně povinni uchovávat po určitou dobu, jako jsou záznamy podrobností o hovorech ([CDR](/mobilnisite/slovnik/cdr/)), informace o poloze a další události související s účastníkem, které jsou následně poskytovány oprávněným subjektům, jako jsou orgány činné v trestním řízení, pro vyšetřovací účely. Funguje na rozhraní HI4.

Z architektonického hlediska přijímá MDF3 archivovaná data nebo záznamy o událostech od síťových funkcí, které tyto informace generují, jako jsou funkce účtování, řízení politik nebo správy mobility. V kontextu 5G to může zahrnovat interakce s funkcí účtování ([CHF](/mobilnisite/slovnik/chf/)), funkcí síťového úložiště ([NRF](/mobilnisite/slovnik/nrf/)) nebo jinými síťovými funkcemi ([NF](/mobilnisite/slovnik/nf/)), které zaznamenávají významné události. Funkce MDF3 shromažďuje, koreluje a formátuje tyto záznamy do standardizované struktury vhodné pro přenos a analýzu. Poté tato data doručí určenému subjektu, často nazývanému Žádající orgán nebo specifický systém pro uchovávání dat, prostřednictvím standardizovaného předávacího rozhraní HI4. Proces je typicky spouštěn zákonnou žádostí, nikoli kontinuálním proudem v reálném čase.

Fungování MDF3 zahrnuje několik klíčových fází. Nejprve musí být zřízena s parametry pro uchovávání dat, jako jsou typy dat ke sběru, doby uchovávání a cílové identity. Po přijetí platné žádosti (často prostřednictvím samostatného administrativního nebo právního rozhraní) MDF3 dotazuje nebo přijímá odeslaná data z příslušných zdrojových síťových funkcí. Provádí úlohy zprostředkování včetně ověření dat, filtrování na základě kritérií žádosti, agregace záznamů souvisejících s jedním účastníkem nebo událostí a převodu do formátu pro doručení (např. standardizované XML schéma). Nakonec bezpečně přenese datový balíček k žádajícímu subjektu, zajišťuje integritu, důvěrnost a poskytuje potvrzení o doručení. MDF3 je klíčová pro umožnění souladu se zákony o uchovávání dat, které vyžadují, aby operátoři ukládali neobsahová data pro potenciální budoucí přístup orgánů, a vyvažuje tak vyšetřovací potřeby s předpisy na ochranu dat.

## K čemu slouží

MDF3 byla vytvořena za účelem formalizace a standardizace mechanismu doručování archivovaných dat v rámci architektury 3GPP pro zákonný odposlech a uchovávání dat. Před její specifikací byly procesy poskytování archivovaných dat (jako jsou historické záznamy hovorů) orgánům činným v trestním řízení často specifické pro operátora, proprietární nebo postrádaly jasné standardizované rozhraní. To vytvářelo neefektivitu pro orgány vyšetřující trestné činy vyžadující historická data a složitosti pro operátory komunikující s více agenturami. MDF3 to řeší definováním jasné, standardizované funkce a rozhraní (HI4) určeného pro tento účel.

Motivace vychází z právních povinností v mnoha jurisdikcích, které vyžadují, aby poskytovatelé telekomunikačních služeb uchovávali specifická neobsahová data (např. kdo komu volal, kdy a odkud) po zákonem stanovenou dobu. Jak se sítě vyvíjely směrem k 5G s její architekturou založenou na službách a síťovým řezáním, zdroje a formáty těchto dat se staly rozmanitějšími a složitějšími. MDF3 poskytuje konzistentní bod zprostředkování, který dokáže sbírat data z nových 5G síťových funkcí, zvládnout objem generovaných dat a doručovat je v předvídatelném formátu. Řeší omezení ad-hoc řešení integrací doručování archivovaných dat do celkové bezpečnostní architektury 3GPP.

Navíc oddělení MDF3 od funkcí pro odposlech v reálném čase ([MDF2](/mobilnisite/slovnik/mdf2/)) umožňuje optimalizovaný návrh systému. Doručování archivovaných dat je typicky méně citlivé na latenci, ale může zahrnovat dotazování na velké databáze a zpracování objemných dat. Díky vyhrazené funkci mohou operátoři sítí přiměřeně škálovat a spravovat zdroje. Její zavedení ve vydání 16 spolu s MDF2 poskytlo komplexní sadu zprostředkovacích funkcí pro všechny aspekty zákonného přístupu, což zajišťuje, že sítě 5G mohly od počátku splňovat povinnosti jak pro odposlech v reálném čase, tak pro uchovávání historických dat.

## Klíčové vlastnosti

- Zprostředkovává doručování archivovaných dat a záznamů o událostech přes rozhraní HI4
- Zpracovává historická, neobsahová data, jako jsou záznamy podrobností o hovorech (CDR) a historie polohy
- Komunikuje se síťovými funkcemi, jako je CHF, pro sběr fakturačních a událostních dat
- Formátuje data do standardizovaných struktur pro oprávněné žádající subjekty
- Podporuje doručování založené na dotazech spouštěných zákonnými žádostmi
- Zajišťuje bezpečný a auditovatelný přenos archivovaných informací o účastnících

## Související pojmy

- [MDF2 – Mediation and Delivery Function 2](/mobilnisite/slovnik/mdf2/)

## Definující specifikace

- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols

---

📖 **Anglický originál a plná specifikace:** [MDF3 na 3GPP Explorer](https://3gpp-explorer.com/glossary/mdf3/)
