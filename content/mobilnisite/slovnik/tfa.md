---
slug: "tfa"
url: "/mobilnisite/slovnik/tfa/"
type: "slovnik"
title: "TFA – TransFer Allowed"
date: 2025-01-01
abbr: "TFA"
fullName: "TransFer Allowed"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tfa/"
summary: "Parametr nebo indikátor v rámci procedur řízení mobility, který signalizuje, zda je povolen přenos kontextu nebo relace účastníka do nového síťového uzlu. Je klíčový pro řízení předávání hovorů/služeb"
---

TFA je parametr v řízení mobility, který signalizuje, zda je povolen přenos kontextu účastníka do nového síťového uzlu, což je klíčové pro řízení předávání hovorů/služeb (handover) a kontinuitu relace.

## Popis

TransFer Allowed (TFA) je řídicí parametr používaný v signalizaci 3GPP jádra sítě, zejména v protokolech řízení mobility a správy relací. Funguje jako příznak nebo informační prvek, který určuje, zda je síť oprávněna přenést aktivní kontext účastníka – jako je kontext [MM](/mobilnisite/slovnik/mm/) (Mobility Management), kontext [PDP](/mobilnisite/slovnik/pdp/) nebo kontext nosiče EPS – z jedné síťové entity do druhé. Tento přenos typicky nastává během předávání mezi systémy (inter-system handover), aktualizací směrovací oblasti nebo změnou obslužného uzlu (např. ze [SGSN](/mobilnisite/slovnik/sgsn/) na jiné SGSN nebo [MME](/mobilnisite/slovnik/mme/)). Parametr vyhodnocují síťové prvky jako [MSC](/mobilnisite/slovnik/msc/), SGSN nebo MME, aby určily přípustnost požadovaného přenosového postupu.

Z architektonického hlediska je TFA zabudován do klíčových signalizačních zpráv. Například v kontextu [GPRS](/mobilnisite/slovnik/gprs/) a UMTS se objevuje ve zprávách jako SGSN Context Request/Response během aktualizace směrovací oblasti mezi SGSN (Inter-SGSN Routing Area Update). Staré SGSN, které drží aktivní kontexty účastníka, použije indikátor TFA, aby informovalo nové SGSN, zda smí přeposlat přesná kontextová data. Nastavení tohoto parametru se řídí síťovými politikami, předplatitelskými daty účastníka a aktuálním stavem relace. Jeho hlavní úlohou je vynucování bezpečnostních a provozních politik, čímž brání neoprávněným nebo nežádoucím přenosům, které by mohly ohrozit integritu relace nebo přesnost účtování.

Mechanismus funguje ve spojení s dalšími parametry, jako je indikátor 'Transfer Restricted'. Když je TFA nastaveno na 'povoleno', zdrojový síťový uzel pokračuje v zabalení a odeslání příslušných kontextových dat (včetně [IMSI](/mobilnisite/slovnik/imsi/), stavu MM, informací o kontextu PDP a bezpečnostních vektorů) do cílového uzlu. Pokud je nastaveno na 'nepovoleno', je přenos zablokován, což může spustit alternativní proceduru, jako je opětovné ověření účastníka od začátku novým uzlem, což může způsobit krátké přerušení služby. Logika rozhodování zahrnuje kontrolu faktorů, jako jsou roamingové dohody sítě, poloha účastníka a zda jsou detekovány podvody nebo bezpečnostní rizika.

Ve vyvinuté paketové jádru (EPC) a 5G jádru (5GC) existují podobné koncepty pod různými názvy a v rámci různých procedur, ale základní princip kontroly autorizace přenosu zůstává. TFA hraje klíčovou roli při zajišťování plynulé mobility při zachování přísné kontroly nad šířením citlivých kontextových informací o účastníkovi. Je to základní kámen pro bezpečné a efektivní provádění předávání hovorů/služeb (handover) napříč generacemi 3GPP sítí.

## K čemu slouží

Parametr TFA byl vytvořen, aby řešil kritické potřeby v mobilním řízení mobility: bezpečnost, provozní kontrolu a kontinuitu služeb. V raných mobilních sítích nekontrolovaný přenos kontextu účastníka mezi síťovými uzly představoval významná bezpečnostní rizika, jako je převzetí kontextu nebo podvodné zřízení relace. TFA poskytuje standardizovaný, politikami řízený mechanismus, který síti umožňuje takové přenosy autorizovat nebo zamítnout, a funguje tak jako strážce pohybu dat účastníka.

Historicky, bez takového řízeného parametru, mohlo předávání mezi uzly v různých administrativních doménách (např. mezi sítěmi různých operátorů) vést k neoprávněnému sdílení dat nebo nesrovnalostem v účtování. TFA umožňuje domovské síti nebo právě obsluhující síti vynucovat své politiky. Například operátor může omezit přenosy při podezření na podvodnou činnost nebo když je vyčerpán kredit účastníka. Řeší problém vyvážení plynulé mobility – která vyžaduje rychlý přenos kontextu – s imperativem zachování síťové bezpečnosti a přesného účtování.

Dále TFA umožňuje složitější síťové architektury a scénáře vzájemného propojení. Je nezbytné pro scénáře jako sdílení sítě, kde více operátorů používá stejnou infrastrukturu RAN, ale má oddělená jádra sítí. Parametr zajišťuje, že kontext účastníka je přenesen pouze do uzlu jádra sítě patřícího operátorovi, ke kterému je účastník přihlášen. Jeho zavedení formalizovalo handshake mezi starým a novým obslužným uzlem, čímž se procedury mobility staly robustnějšími, předvídatelnějšími a bezpečnějšími, což byla nutná evoluce, jak se sítě stávaly složitějšími a vzájemně propojenějšími.

## Klíčové vlastnosti

- Binární indikátor autorizující nebo zakazující přenos kontextu účastníka
- Používá se v signalizaci mezi uzly (např. mezi SGSN, MME)
- Vynucuje síťovou bezpečnost a politiky během událostí mobility
- Ovlivňuje úspěšnost předání hovoru/služby (handover) a kontinuitu služeb
- Vyhodnocuje se na základě předplatného, polohy a stavu sítě
- Zabraňuje neoprávněnému šíření citlivých dat relace

## Související pojmy

- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [TFA na 3GPP Explorer](https://3gpp-explorer.com/glossary/tfa/)
