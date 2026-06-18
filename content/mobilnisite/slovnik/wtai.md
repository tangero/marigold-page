---
slug: "wtai"
url: "/mobilnisite/slovnik/wtai/"
type: "slovnik"
title: "WTAI – Wireless Telephony Applications Interface"
date: 2025-01-01
abbr: "WTAI"
fullName: "Wireless Telephony Applications Interface"
category: "Interface"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wtai/"
summary: "Knihovna programového rozhraní pro WTA, která poskytuje specifická funkční volání umožňující aplikacím ovládat telefonní funkce na mobilním zařízení. Definuje způsob interakce softwaru s funkcemi síťo"
---

WTAI je knihovna programového rozhraní pro aplikace bezdrátové telefonie, která poskytuje funkční volání umožňující softwaru ovládat telefonní funkce mobilního zařízení, jako například uskutečňování hovorů a zpracování zpráv.

## Popis

Wireless Telephony Applications Interface (WTAI) je konkrétní soubor knihoven a funkčních volání implementující framework Wireless Telephony Applications ([WTA](/mobilnisite/slovnik/wta/)). Je v podstatě [API](/mobilnisite/slovnik/api/), které vývojáři aplikací používají k vytváření programů, které mohou komunikovat s telefonními a síťovými schopnostmi mobilního telefonu. WTAI je zpřístupněno WTA User Agentu na zařízení, který vykonává WMLScript nebo [WML](/mobilnisite/slovnik/wml/) stránky obsahující WTAI funkční volání. Tyto volání jsou rozděleny do různých knihoven, například Public WTAI knihovna pro běžné funkce a Network Common WTAI pro funkce specifické pro operátora.

Technicky WTAI funguje definováním namespace a série funkčních signatur, které jsou svázány s nativním telefonním softwarem zařízení. Například WMLScript může obsahovat volání `WTAPublic.makeCall("123456789")`. WTA User Agent zachytí tento volání, ověří jej proti bezpečnostním politikám a následně vyvolá odpovídající nativní platformní funkci k iniciaci procesu vytáčení. Rozhraní také zpracovává asynchronní události; například při příchodu hovoru může síť pushovat service indication, která spustí WTAI event handler v aplikaci. To umožňuje aplikacím reagovat na síťové události v reálném čas.

Knihovny v rámci WTAI pokrývají široký rozsah telefonních funkcí: řízení hovorů (iniciování, přijímání, přepojování), síťové zasílání zpráv (odesílání a přijímání [SMS](/mobilnisite/slovnik/sms/)), správa telefonního seznamu (čtení a zápis položek) a generování [DTMF](/mobilnisite/slovnik/dtmf/) tónů. Klíčový architektonický aspekt je oddělení mezi public funkcemi, které jsou obecně dostupné, a network-specific funkcemi, které mohou vyžadovat souhlas operátora nebo secure kontext. WTAI také obsahuje funkce pro správu WTA repository a zpracování channel managementu pro datové spojení. Jeho role byla poskytnout standardizovanou, nezávislou na zařízení abstraktní vrstvu, která chránila vývojáře od komplexity podkladových hardware-specific AT příkazů nebo proprietárních OS API.

## K čemu slouží

WTAI byl vytvořen, aby poskytoval uniformní, standardizované programové rozhraní pro telefonní funkce na všech WTA-kompatibilních mobilních zařízeních. Před WTAI přístup k telefonním funkcím, jako vytáčení nebo zasílání zpráv z aplikace, vyžadoval použití protokolů specifických pro výrobce nebo low-level AT příkazů, což vedlo k fragmentaci a vysokým nákladům na vývoj. [WAP](/mobilnisite/slovnik/wap/) Forum a 3GPP vytvořily WTAI k řešení tohoto problému interoperability, umožňující vývojářům napsat jednu aplikaci, která může běžet na jakémkoliv podporovaném telefonu.

Primární problém, který řešil, byl absence bezpečného, síťově-aware [API](/mobilnisite/slovnik/api/) pro služby s přidanou hodnotou. Operátory chtěly nasazovat služby jako jedno-click vytáčení z webové stránky nebo vizual voicemail, ale potřebovali záruku, že tyto aplikace nezpůsobí crash telefonu nebo nezneužijí síťové zdroje. WTAI poskytoval kontrolovaný sandbox s dobře definovanými funkcemi a bezpečnostními sémantikami. Jeho vytvoření bylo motivované konvergence telefonie a datových služeb v 2.5G a 3G síťích, kde vylepšení základního hlasového hovoru s datově-driven funkcemi se stalo klíčovým konkurenčním diferenciátorem. Standardizací rozhraní také facilitoval testování a certifikaci zařízení a aplikací, zajišťující konzistentní uživatelský experience.

## Klíčové vlastnosti

- Knihovna funkčních volání pro nastavení, řízení a ukončení hovoru
- API pro odesílání a přijímání SMS a dalších síťových zpráv
- Rozhraní pro přístup a modifikaci položek telefonního seznamu a záznamů hovorů zařízení
- Funkce pro generování DTMF tónů během hovoru
- Zpracování událostí pro síťově-iniciované telefonní události
- Bezpečný kontext a řízení přístupu pro citlivé telefonní operace

## Související pojmy

- [WTA – Wireless Telephony Applications](/mobilnisite/slovnik/wta/)
- [WAP – Wireless Application Protocol](/mobilnisite/slovnik/wap/)
- [SAT – SIM Application Toolkit](/mobilnisite/slovnik/sat/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification

---

📖 **Anglický originál a plná specifikace:** [WTAI na 3GPP Explorer](https://3gpp-explorer.com/glossary/wtai/)
