---
slug: "emmi"
url: "/mobilnisite/slovnik/emmi/"
type: "slovnik"
title: "EMMI – Electrical Man Machine Interface"
date: 2025-01-01
abbr: "EMMI"
fullName: "Electrical Man Machine Interface"
category: "Management"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/emmi/"
summary: "EMMI označuje standardizované elektrické a fyzické rozhraní (konektor) na mobilním zařízení, primárně pro připojení příslušenství, jako jsou nabíječky a datové kabely. Jeho standardizace zajišťuje int"
---

EMMI je standardizovaný elektrický a fyzický konektor na mobilním zařízení pro příslušenství, jako jsou nabíječky a datové kabely, zajišťující interoperabilitu a bezpečnost.

## Popis

Elektrické rozhraní člověk-stroj (EMMI) v terminologii 3GPP specifikuje fyzický konektor a související elektrické charakteristiky na uživatelském zařízení (UE) – typicky mobilním telefonu – pro připojení k externím zařízením nebo zdrojům napájení. Jde o standard hardwarového rozhraní, podrobně popsaný ve specifikacích jako TS 31.121, který definuje požadavky na konektory používané pro nabíjení, přenos dat a audio připojení. Primárním cílem je zajistit, aby příslušenství od různých výrobců bylo interoperabilní s mobilními zařízeními, která deklarují shodu, čímž se zlepšuje uživatelský zážitek a snižuje se množství elektronického odpadu.

Specifikace EMMI pokrývá několik klíčových aspektů. Definuje mechanické vlastnosti konektoru, včetně jeho tvaru, rozměrů, pinoutu a požadavků na odolnost. Z elektrického hlediska specifikuje úrovně napětí a proudu pro nabíjení, signalizační protokoly pro detekci příslušenství (např. rozlišení nabíječky od datového kabelu) a charakteristiky datových vedení pro protokoly jako [USB](/mobilnisite/slovnik/usb/). Bezpečnost je kritickou součástí, s požadavky na ochranu proti přepětí, odolnost proti zkratu a tepelné řízení, aby se předešlo nebezpečí během nabíjení nebo synchronizace dat.

V praxi se EMMI vyvinulo z proprietárních konektorů na široce přijímané průmyslové standardy. Zatímco rané odkazy 3GPP mohly být obecnější, tato práce se sladila s běžnými typy konektorů, jako je Micro-USB a později USB-C, a často na ně odkazuje. Proces standardizace zahrnuje zajištění, že rozhraní na UE může spolehlivě podporovat požadované funkce, jako je nabíjení ze společného externího napájecího zdroje (EPS) a připojení k osobní síti ([PAN](/mobilnisite/slovnik/pan/)) pro sdílení internetového připojení nebo přenos souborů. Shoda se specifikacemi EMMI je často ověřována prostřednictvím testů shody, jak je popsáno v dokumentech jako TS 38.509, aby bylo zaručeno, že zařízení splňují nezbytné standardy interoperability a bezpečnosti před uvedením na trh.

## K čemu slouží

EMMI bylo standardizováno za účelem řešení významného problému proprietárních konektorů pro nabíjení a data na počátku trhu s mobilními telefony. Před standardizací používal každý výrobce často jedinečný konektor, což nutilo spotřebitele vlastnit více nabíječek a kabelů, způsobovalo nepohodlí, zvyšovalo množství elektronického odpadu a fragmentovalo trh s příslušenstvím. Z pohledu operátora a regulátora to také komplikovalo certifikaci zařízení a logistiku. Primárním účelem specifikace EMMI bylo nařídit společné fyzické rozhraní, aby se zajistila interoperabilita, zvýšilo uživatelské pohodlí a podpořila environmentální udržitelnost snížením počtu potřebných nabíječek.

K jeho vytvoření vedly regulační tlaky a průmyslové iniciativy (jako je snaha EU o společnou nabíječku) s cílem harmonizovat rozhraní. 3GPP jako orgán standardizující UE převzal úlohu definovat technické požadavky, aby zajistil, že rozhraní bude fungovat nejen mechanicky, ale také splní bezpečnostní standardy pro elektrická připojení. Vyřešilo to omezení předchozího ad-hoc přístupu tím, že poskytlo jednotnou technickou specifikaci, kterou mohli výrobci zařízení implementovat, a zajistilo, že jakákoli kompatibilní nabíječka nebo datový kabel bude fungovat s jakýmkoli kompatibilním telefonem bez ohledu na značku. To také usnadnilo vývoj konkurenceschopného, interoperabilního ekosystému příslušenství třetích stran.

## Klíčové vlastnosti

- Definuje typ fyzického konektoru, jeho rozměry a konfiguraci pinů
- Specifikuje elektrické parametry pro bezpečné nabíjení (napětí, proud)
- Zahrnuje požadavky na logiku detekce a identifikace příslušenství
- Ukládá bezpečnostní ochrany proti přepětí, nadproudu a zkratům
- Podporuje možnosti přenosu dat, často v souladu se standardy USB
- Zajišťuje mechanickou odolnost pro stanovený počet připojovacích cyklů

## Související pojmy

- [UE – User Equipment](/mobilnisite/slovnik/ue/)
- [USB – Universal Serial Bus](/mobilnisite/slovnik/usb/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification
- **TS 38.509** (Rel-18) — Special conformance testing functions for UE

---

📖 **Anglický originál a plná specifikace:** [EMMI na 3GPP Explorer](https://3gpp-explorer.com/glossary/emmi/)
