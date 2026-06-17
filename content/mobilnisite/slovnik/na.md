---
slug: "na"
url: "/mobilnisite/slovnik/na/"
type: "slovnik"
title: "NA – No Audio-alerting capability"
date: 2026-01-01
abbr: "NA"
fullName: "No Audio-alerting capability"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/na/"
summary: "Indikátor doplňkové služby označující, že uživatel nebo zařízení nemá schopnost generovat zvukové upozornění na příchozí hovor. Modifikuje procedury zpracování hovoru a často spouští alternativní meto"
---

NA je indikátor doplňkové služby označující, že uživatel nebo zařízení nemá schopnost generovat zvukové upozornění na příchozí hovor.

## Popis

No Audio-alerting capability (NA) je funkce doplňkové služby v rámci specifikací telefonie 3GPP pro okruhově přepínané sítě a IP Multimedia Subsystem (IMS). Jedná se o schopnost účastníka nebo terminálu, která indikuje neschopnost vytvořit slyšitelný vyzváněcí tón nebo upozornění na příchozí hlasový hovor. Tato schopnost je registrována v síti, typicky na Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo v řídicí funkci služby. Když je hovor směrován k účastníkovi označenému NA, síť modifikuje standardní procedury navazování hovoru. Namísto odesílání zpráv pro upozornění (alerting) za účelem spuštění vyzvánění terminálu může síť hovor okamžitě přepojit na hlasovou schránku, prezentovat volajícímu obsazovací tón nebo vyzkoušet alternativní mechanismy upozornění definované logikou služby.

Technická operace zahrnuje logiku řízení služby v rámci Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) pro okruhově přepínané hovory nebo Serving-Call Session Control Function (S-CSCF) v IMS. Během dokončování hovoru síť kontroluje profil účastníka na přítomnost indikátoru NA. Pokud je aktivní, síť potlačí normální signál 'Alerting' (v IMS SIP 180 Ringing), který by byl odeslán volající straně a volanému terminálu. Místo toho může vyvolat službu, jako je Call Completion to Busy Subscriber ([CCBS](/mobilnisite/slovnik/ccbs/)), nebo hovor přímo připojit k serveru s hlasovým oznámením či k systému zasílání zpráv. Volaná strana může obdržet neslyšitelné upozornění, například záblesk na obrazovce, textovou zprávu nebo datový příkaz indikující zmeškaný hovor, v závislosti na schopnostech terminálu a předplatném služby.

Z architektonického hlediska NA interaguje s dalšími doplňkovými službami, jako je Call Forwarding a Message Waiting Indication ([MWI](/mobilnisite/slovnik/mwi/)). Její implementace je detailně popsána napříč více specifikacemi 3GPP pokrývajícími požadavky na služby (řada 22), detaily protokolů (řada 24 pro [CS](/mobilnisite/slovnik/cs/), řada 29 pro IMS Diameter a SIP) a správu (řada 32). Tato funkce je klíčová pro přístupnost, neboť umožňuje uživatelům, kteří jsou neslyšící nebo nedoslýchaví, efektivně využívat telefonní služby. Má také uplatnění ve scénářích, kde jsou slyšitelná upozornění nežádoucí, například v nemocnicích, knihovnách nebo u zařízení ve službě používajících pouze vibrační režim. Zpracování sítí zajišťuje, že volající strana obdrží odpovídající zpětnou vazbu a volaná strana je upozorněna přístupnými prostředky, čímž je zachována funkčnost telefonní služby při současném přizpůsobení se nedostatku zvukového upozornění.

## K čemu slouží

Schopnost No Audio-alerting capability (NA) byla vytvořena, aby zajistila, že telefonní služby jsou přístupné a funkční pro všechny uživatele, včetně osob se sluchovým postižením. Jejím primárním účelem je modifikovat standardní proces upozorňování na hovor tak, aby vyhovoval terminálům nebo uživatelům, kteří nemohou vnímat slyšitelné vyzvánění. Bez této služby by hovor k neslyšícímu uživateli vedl k nezaznamenanému vyzvánění telefonu, které by nakonec vypršelo a hovor by byl přepojen na hlasovou schránku, aniž by volaná strana obdržela bezprostřední přístupné upozornění. NA tento problém řeší tím, že umožňuje síti zasáhnout a poskytnout alternativní, přístupnou formu upozornění na hovor nebo jeho okamžité zpracování.

Historicky, jak se telefonie vyvíjela od základních okruhově přepínaných služeb k funkcím inteligentní sítě a později k IMS, se potřeba inkluzivního designu stala regulační a etickou nutností. Funkce NA, zavedená v raných vydáních 3GPP, řeší omezení tradičního modelu upozorňování. Umožňuje poskytovatelům služeb nabízet odpovídající služby přístupnosti, často vyžadované národními předpisy. Funkce má také praktické aplikace přesahující přístupnost, například v komunikaci typu stroj-stroj (M2M), kde zařízení nemají reproduktor, nebo ve specializovaných uživatelských prostředích, kde musí být zvuk minimalizován.

Dále NA usnadňuje integraci telefonie s dalšími systémy upozornění. Umožňuje, aby hovory spouštěly vizuální signály na specializovaných terminálech, textové zprávy na pager nebo sekundární zařízení, nebo aktualizace indikátorů čekajících zpráv. To překlenuje propast mezi čistě hlasovou telefonií a multimodální komunikací, což je v souladu s trendem konvergence v moderní telekomunikaci. Tím, že řeší základní problém upozorňování bez zvuku, podporuje princip univerzální služby a umožňuje inovativní aplikace pro zpracování hovorů pro různé uživatelské potřeby a typy zařízení.

## Klíčové vlastnosti

- Indikátor doplňkové služby uložený v profilu účastníka
- Modifikuje procedury dokončování hovoru za účelem potlačení signálů zvukového upozornění
- Může spustit okamžité přepojení hovoru na hlasovou schránku nebo hlasové oznámení
- Umožňuje alternativní metody upozornění, jako jsou vizuální signalizace nebo zprávy
- Integruje se s dalšími doplňkovými službami (např. Call Forwarding, MWI)
- Podporováno jak v okruhově přepínaném jádru, tak v telefonii založené na IMS

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 22.889** (Rel-17) — FRMCS Study; Stage 1
- **TR 22.989** (Rel-20) — FRMCS Analysis and Requirements
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 26.404** (Rel-19) — Enhanced aacPlus SBR Encoder Specification
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TS 28.821** (Rel-13) — UML Model Repertoire for FMC Management
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4
- **TS 29.334** (Rel-19) — IMS-ALG to IMS-AGW Interface Protocol
- **TS 31.111** (Rel-19) — USIM Application Toolkit (USAT) Specification
- **TS 32.156** (Rel-20) — UML Modeling for Network Management Systems

---

📖 **Anglický originál a plná specifikace:** [NA na 3GPP Explorer](https://3gpp-explorer.com/glossary/na/)
