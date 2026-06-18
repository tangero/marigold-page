---
slug: "bc1"
url: "/mobilnisite/slovnik/bc1/"
type: "slovnik"
title: "BC1 – Bearer Capability 1"
date: 2025-01-01
abbr: "BC1"
fullName: "Bearer Capability 1"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bc1/"
summary: "BC1 je parametr v signalizaci řízení volání, který udává preferovanou službu přenosu pro spojení v přepojování okruhů. Používá se při sestavování hovoru k určení typu přenosu (např. řeč, data), který"
---

BC1 je signalizační parametr řízení volání, který udává preferovanou službu přenosu v přepojování okruhů požadovanou při sestavování hovoru, například řeč nebo data, pro přidělování zdrojů v sítích GSM a UMTS.

## Popis

Bearer Capability 1 (BC1) je základním informačním prvkem v protokolu řízení volání 3GPP, konkrétně používaným ve zprávě SETUP pro hovory v přepojování okruhů ([CS](/mobilnisite/slovnik/cs/)). Nachází se v informačním prvku Bearer Capability, který popisuje charakteristiky služby přenosu požadované uživatelským zařízením (UE) pro hlasový nebo datový hovor. Parametr BC1 je definován jako 'první' nebo preferovaná přenosová schopnost, což umožňuje UE signalizovat síti svůj hlavní požadavek na službu. Síť tyto informace spolu s dalšími parametry v [IE](/mobilnisite/slovnik/ie/) Bearer Capability používá k provádění kontroly kompatibility, přidělování zdrojů a funkcí vzájemného propojení.

Z architektonického hlediska BC1 zpracovává ústředna mobilního přepojování ([MSC](/mobilnisite/slovnik/msc/)) v jádru sítě GSM/UMTS. Když UE zahájí hovor iniciovaný z mobilního zařízení, zahrne informační prvek Bearer Capability do zprávy SETUP odeslané přes rozhraní rádiového přístupu (prostřednictvím subsystému základnových stanic) do MSC. MSC analyzuje hodnotu BC1, aby určila typ požadované služby přenosu – například řeč, neomezené digitální informace ([UDI](/mobilnisite/slovnik/udi/)) pro data v přepojování okruhů nebo 3,1 kHz audio. Tato analýza je klíčová pro MSC, aby vybrala správný kodek, přidělila vhodný kanál pro přenos ([TCH](/mobilnisite/slovnik/tch/)) a vytvořila kompatibilní spojení prostřednictvím sítě, případně zahrnující vzájemné propojení s telefonní sítí s komutovanými okruhy ([PSTN](/mobilnisite/slovnik/pstn/)) nebo jinými [PLMN](/mobilnisite/slovnik/plmn/).

Technicky je parametr BC1 zakódován jako bitové pole ve struktuře IE Bearer Capability definované v 3GPP TS 24.008. Jeho hodnota odpovídá konkrétní službě přenosu definované v doporučeních řady [ITU-T](/mobilnisite/slovnik/itu-t/) I.200, která jsou namapována do specifikací 3GPP. Například hodnota BC1 označující 'řeč' sděluje síti, aby se připravila na hlasový hovor pomocí řečového kodeku jako je AMR nebo EFR. Odpověď sítě ve zprávě CALL PROCEEDING nebo ALERTING může obsahovat IE Bearer Capability s potvrzenou hodnotou BC1, která udává službu přenosu, která bude skutečně použita, a která se může lišit od požadavku kvůli možnostem sítě nebo vyjednávání.

Role BC1 přesahuje pouhou indikaci služby; je nedílnou součástí procedur vzájemného propojení služeb a přepojování zpět. Ve scénářích, jako je přepojování zpět na přepojování okruhů (CSFB) z LTE, UE zahrne BC1 do zprávy SETUP, aby při přechodu na síť 2G/3G indikovalo požadovanou CS službu (např. hlas). Dále BC1 podporuje kompatibilitu signalizace DTMF a vzájemné propojení modemů pro faxové/datové hovory specifikací odpovídajícího typu přenosu. Jeho správná interpretace zajišťuje kompatibilitu služby a kvalitu služby (QoS) koncové služby pro uživatele, což z něj činí základní kámen tradičních telekomunikačních služeb v přepojování okruhů v sítích 2G a 3G.

## K čemu slouží

BC1 byl vytvořen, aby umožnil diferenciaci služeb a spolehlivé sestavování hovorů v raných digitálních celulárních sítích, jako je GSM. Před standardizací existovala potřeba strukturovaného způsobu, jak mobilní terminál mohl signalizovat, jaký typ komunikační služby hodnavést – zda standardní hlasový hovor, datový hovor používající modem nebo faxový přenos. Informační prvek Bearer Capability, s BC1 jako klíčovou součástí, tento mechanismus poskytl, což umožnilo síti porozumět požadavkům na službu a přidělit odpovídající síťové zdroje (např. plný kanál pro přenos pro řeč versus kanál optimalizovaný pro data).

Řešil problém nekompatibility služeb a neefektivního využívání zdrojů. Bez přesné indikace přenosové schopnosti by síť mohla pro všechny hovory předpokládat výchozí službu (jako je řeč), což by vedlo k neúspěšným datovým spojením nebo špatné kvalitě hlasu. BC1 umožnil explicitní vyjednávání, což zajišťovalo, že pokud uživatel chtěl uskutečnit datový hovor, síť se nepokusila použít řečové kompresní kodeky, které by poškodily datový tok. To bylo obzvláště důležité pro rané mobilní datové služby a fax přes celulární síť, které vyžadovaly transparentní digitální kanály.

Historicky definice BC1 ve verzi 99 (a její převzetí z GSM Phase 2+) vytvořila základ pro řízení služeb v přepojování okruhů, který přetrval v UMTS. Řešila omezení analogových systémů a raných digitálních protokolů, kterým chyběly podrobné deskriptory služeb. Jak se sítě vyvíjely směrem k plně IP v LTE a 5G, relevance BC1 pro nativní služby v přepojování paketů poklesla, ale zůstala kritická pro interoperabilitu se staršími CS systémy, CSFB a zajištění zpětné kompatibility pro hlasové služby během přechodu na VoLTE a VoNR.

## Klíčové vlastnosti

- Udává preferovaný typ služby přenosu v přepojování okruhů (např. řeč, UDI, 3,1 kHz audio) při sestavování hovoru
- Zakódován v informačním prvku Bearer Capability signalizačních zpráv řízení volání (např. SETUP)
- Používán MSC pro přidělování zdrojů, výběr kodeku a rozhodování o vzájemném propojení
- Podporuje vyjednávání služeb a kontrolu kompatibility mezi UE a sítí
- Nezbytný pro procedury přepojování zpět na přepojování okruhů (CSFB) z LTE na 2G/3G
- Umožňuje vzájemné propojení s PSTN a staršími datovými službami (fax, modem)

## Související pojmy

- [CSFB – Circuit Switched Fallback](/mobilnisite/slovnik/csfb/)

## Definující specifikace

- **TS 23.172** (Rel-19) — Service Change and UDI Fallback (SCUDIF)
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G

---

📖 **Anglický originál a plná specifikace:** [BC1 na 3GPP Explorer](https://3gpp-explorer.com/glossary/bc1/)
