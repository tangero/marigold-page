---
slug: "mves"
url: "/mobilnisite/slovnik/mves/"
type: "slovnik"
title: "MVES – MCVideo Emergency State"
date: 2025-01-01
abbr: "MVES"
fullName: "MCVideo Emergency State"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mves/"
summary: "Funkční stav v klientovi a serveru MCVideo, který se aktivuje, když uživatel zahájí nouzovou videoakci (např. MVEPC). Mění chování klienta a síťové zpracování tak, aby upřednostňovalo veškerou následn"
---

MVES je funkční stav aktivovaný v klientovi a serveru MCVideo během nouzového videohovoru, který upřednostňuje veškerou následnou komunikaci daného uživatele.

## Popis

[MCVideo](/mobilnisite/slovnik/mcvideo/) Emergency State (MVES) je logický a funkční stav, do kterého vstoupí klient služby Mission Critical Service (např. aplikace MCVideo) uživatele a který rozpozná síťový Mission Critical Server. Je spuštěn explicitní akcí uživatele k zahájení nouzové služby, nejčastěji začátkem nouzového privátního videohovoru MCVideo ([MVEPC](/mobilnisite/slovnik/mvepc/)). Vstup do MVES je klíčovou událostí, která mění provozní parametry a síťové zpracování veškeré komunikace od tohoto uživatele po dobu trvání nouzové události.

Z architektonického hlediska je přechod stavu řízen společně mezi [MC](/mobilnisite/slovnik/mc/) klientem a MCVideo serverem. Když uživatel spustí nouzový videohovor, klientská aplikace odešle konkrétní servisní požadavek (např. žádost o zahájení nouzové relace dle TS 24.281) na MCVideo server. Po ověření žádosti a zahájení nastavování hovoru server potvrdí a potvrdí aktivaci MVES pro daného uživatele. Tento stav je pak udržován jak v klientovi, tak na serveru. Uživatelské rozhraní klienta se může změnit (např. zobrazením výrazného indikátoru 'EMERGENCY') a jeho chování je upraveno – například může automaticky přijímat příchozí nouzovou komunikaci nebo omezovat nenouzové akce.

Z pohledu sítě má deklarace MVES významné důsledky. Informuje MCVideo server a následně i politiky core sítě, že provoz tohoto uživatele by měl být zpracován s nejvyšší prioritou, a to nejen pro počáteční hovor, ale pro veškerou následnou komunikaci. To znamená, že i když počáteční relace MVEPC skončí, uživatel může zůstat v MVES a jakýkoli nový videohovor nebo datová relace, kterou zahájí, může nadále dostávat nouzovou prioritu QoS (řízenou mechanismy jako [MVEPP](/mobilnisite/slovnik/mvepp/)), dokud oprávněná osoba (uživatel nebo dispečer) výslovně nezruší nouzový stav. Server tento stav spravuje, případně vysílá nouzový stav uživatele dalším autorizovaným uživatelům (jako je skupina dispečerů) a zaznamenává všechny aktivity pro analýzu po události. Zrušení MVES zahrnuje specifický postup deaktivace, který vrátí uživatele a jeho služby na normální úroveň priority.

## K čemu slouží

MVES existuje, aby poskytoval kontext a trvání nouzovým operacím nad rámec jedné relace hovoru. Problém, který řeší, je potenciální fragmentace nouzové reakce; bez trvalého stavu by záchranář mohl navázat vysoce prioritní [MVEPC](/mobilnisite/slovnik/mvepc/), ale jakmile tento hovor skončí, jeho další komunikace (např. odeslání důležitého snímku nebo zahájení nového hovoru) by mohla neúmyslně přejít na normální prioritu, což by způsobilo nebezpečná zpoždění. MVES zajišťuje kontinuitu prioritního zpracování po celou dobu trvání nouzové události.

Tento koncept byl motivován provozními protokoly z tradičních pozemních mobilních rádiových systémů, kde 'nouzový režim' nebo stav 'man-down' přetrvává, dokud není zrušen. Přenesení tohoto konceptu do IP-broadbandových systémů vyžadovalo standardizovaný stavový stroj na servisní vrstvě. MVES řeší omezení čistě relace-centrického modelu QoS tím, že váže prioritu na provozní stav uživatele. Poskytuje jasný, jednoznačný signál celému systému mission-critical, že konkrétní uživatel je zapojen do životně kritické situace, což umožňuje koordinovanou a prioritní podporu jak ze strany sítě, tak od ostatních lidských operátorů, dokud není situace formálně vyřešena. Je to klíčová vlastnost pro zajištění robustnosti a provozní praktičnosti služeb [MCVideo](/mobilnisite/slovnik/mcvideo/) pro reálné nasazení v oblasti veřejné bezpečnosti.

## Klíčové vlastnosti

- Trvalý stav na servisní vrstvě aktivovaný nouzovou akcí uživatele
- Mění chování klientské aplikace a UI během nouzových událostí
- Zajišťuje kontinuitu vysoké priority QoS pro veškerou komunikaci uživatele, dokud je aktivní
- Spravován a koordinován MCVideo serverem
- Vyžaduje explicitní akci uživatele nebo dispečera k deaktivaci
- Může být signalizován dalším autorizovaným uživatelům v rámci systému mission-critical

## Související pojmy

- [MVEPC – MCVideo Emergency Private Call](/mobilnisite/slovnik/mvepc/)

## Definující specifikace

- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [MVES na 3GPP Explorer](https://3gpp-explorer.com/glossary/mves/)
