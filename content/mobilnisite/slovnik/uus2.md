---
slug: "uus2"
url: "/mobilnisite/slovnik/uus2/"
type: "slovnik"
title: "UUS2 – User-to-User Signalling Service 2"
date: 2025-01-01
abbr: "UUS2"
fullName: "User-to-User Signalling Service 2"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/uus2/"
summary: "Součást doplňkové služby UUS, která umožňuje volanému uživateli odeslat uživatelské informace zpět volajícímu během fáze zřizování hovoru, typicky v rámci zprávy ALERTING nebo CONNECT. To umožňuje vol"
---

UUS2 je doplňková služba, která umožňuje volanému uživateli odeslat informaci zpět volajícímu uživateli v rámci zpráv pro zřízení hovoru, jako jsou ALERTING nebo CONNECT.

## Popis

User-to-User Signalling Service 2 (UUS2) je komplementární službou k [UUS1](/mobilnisite/slovnik/uus1/) v rámci rodiny doplňkových služeb [UUS](/mobilnisite/slovnik/uus/). Zatímco UUS1 umožňuje přenos dat od volajícího k volanému při zřizování hovoru, UUS2 umožňuje volané straně odeslat uživatelské informace zpět volajícímu během fáze zřizování hovoru. Tento přenos je iniciován terminálem volaného uživatele a probíhá poté, co volaná strana obdrží žádost o zřízení hovoru (SETUP), ale před plným připojením hovoru. Technicky terminál volaného zahrne informační prvek User-to-User (UUIE) do své odpovědní zprávy odesílané zpět směrem k volajícímu – typicky zprávy ALERTING (signalizující, že terminál volaného vyzváněl uživatele) nebo CONNECT (signalizující přijetí hovoru).

Síť tento UUIE transparentně přenáší v opačném směru v rámci odpovídajících zpráv [ISUP](/mobilnisite/slovnik/isup/), jako je Address Complete Message ([ACM](/mobilnisite/slovnik/acm/)) pro ALERTING nebo Answer Message ([ANM](/mobilnisite/slovnik/anm/)) pro CONNECT. Terminál volajícího uživatele přijme UUIE vložený ve zprávě ALERTING nebo CONNECT od sítě a může tyto informace prezentovat uživateli nebo aplikaci. Stejně jako u UUS1 je obsah definován uživatelem a není interpretován sítí, která pouze provádí kontrolu předplatného služby. Služba je asociovaná s hovorem, což znamená, že přenos dat je vnitřně propojen s úspěšným průběhem signalizační sekvence pro zřízení hovoru.

Z architektonického hlediska vyžaduje aktivace UUS2, aby měl volaný předplatitel službu zřízenou ve svém profilu v [HLR](/mobilnisite/slovnik/hlr/). Obsluhující [MSC](/mobilnisite/slovnik/msc/) pro volanou stranu toto ověří předtím, než povolí zahrnutí UUIE do odchozí odpovědní zprávy. Na protokolové vrstvě je UUIE vložen do zprávy [DSS1](/mobilnisite/slovnik/dss1/) ALERTING nebo CONNECT na rozhraní uživatel-síť. Pro přenos přes síť je namapován do parametru User-to-User příslušné zprávy ISUP. UUS2 lze používat nezávisle na UUS1; hovor může zahrnovat pouze UUS2, pouze UUS1 nebo obojí, v závislosti na službách předplatitele a možnostech terminálu. Služba je užitečná zejména pro poskytování vyzváněcích tónů s daty, odesílání odpovědí pro autentizaci volajícího nebo signalizaci důvodu opožděného přijetí hovoru.

## K čemu slouží

UUS2 byla vytvořena k řešení potřeby obousměrné výměny dat během zřizování hovoru, což umožňuje volané straně odpovědět volajícímu kontextovými informacemi. Před UUS2 neměl volaný uživatel nebo zařízení standardizovaný mechanismus pro odeslání dat zpět volajícímu před zřízením hlasové cesty, kromě tónů v pásmu nebo hlášení po přijetí hovoru. To bylo omezením pro interaktivní hlasové systémy, zabezpečené procedury zpětného volání nebo situace, kdy volaná strana chtěla naznačit stav (např. 'Odpovím za 30 sekund' nebo 'Zadejte svůj PIN').

Doplňovala UUS1 a vytvářela tak jednoduchý mechanismus požadavek-odpověď plně v rámci signalizačního kanálu, což snižovalo čas interakce po přijetí hovoru. Služba měla za cíl zlepšit automatizované telefonní aplikace a komunikaci člověk-stroj v éře před VoIP. Její rozšíření však bylo, podobně jako u UUS1, omezeno potřebou široké podpory terminálů a sítí, a zůstala okrajovou funkcí používanou primárně ve specifických korporátních scénářích nebo scénářích propojování sítí, než byla zastíněna signalizačními možnostmi založenými na IP.

## Klíčové vlastnosti

- Přenos uživatelských informací iniciovaný volanou stranou během zřizování hovoru
- Uživatelská data jsou přenášena v rámci zpráv ALERTING nebo CONNECT a odpovídajících zpráv ISUP ACM/ANM
- Umožňuje odpověď nebo kontext od volané strany před přijetím hovoru nebo při něm
- Vyžaduje zřízení předplatného pro volanou stranu
- Funguje transparentně s ověřením předplatného v síti
- Podporuje nezávislé použití od UUS1, což umožňuje flexibilní signalizační vzory asociované s hovorem

## Související pojmy

- [UUS – User-to-User Signalling Supplementary Service](/mobilnisite/slovnik/uus/)
- [UUS1 – User-to-User Signalling Service 1](/mobilnisite/slovnik/uus1/)
- [ACM – Association for Computing Machinery](/mobilnisite/slovnik/acm/)
- [ANM – Answer Message](/mobilnisite/slovnik/anm/)

## Definující specifikace

- **TS 23.087** (Rel-19) — User-to-User Signalling (UUS) Stage 2
- **TS 24.087** (Rel-19) — User-to-User Signalling (UUS) Stage 3

---

📖 **Anglický originál a plná specifikace:** [UUS2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/uus2/)
