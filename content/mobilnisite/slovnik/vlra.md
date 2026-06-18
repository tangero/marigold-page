---
slug: "vlra"
url: "/mobilnisite/slovnik/vlra/"
type: "slovnik"
title: "VLRA – Visitor Location Register for the A-subscriber"
date: 2025-01-01
abbr: "VLRA"
fullName: "Visitor Location Register for the A-subscriber"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/vlra/"
summary: "Konkrétní VLR, který v aktuálně probíhající komunikaci iniciované z mobilní sítě obsluhuje volající stranu (A-účastníka). Jedná se o funkční označení používané v rámci procedur řízení hovoru a účtován"
---

VLRA (Visitor Location Register pro A-účastníka) je návštěvnický registr polohy, který v aktuálně probíhajícím hovoru iniciovaném z mobilní sítě obsluhuje volající stranu (A-účastníka). Používá se v rámci řízení hovoru a účtování k identifikaci síťového uzlu tohoto původního uživatele.

## Popis

VLRA není samostatný fyzický síťový prvek, ale logická role přiřazená standardnímu [VLR](/mobilnisite/slovnik/vlr/) v kontextu konkrétního hovoru nebo nastavování relace. Ve specifikacích 3GPP, zejména těch zabývajících se řízením hovoru (např. TS 23.018) a logikou služeb Camel, se termíny 'VLRA' a '[VLRB](/mobilnisite/slovnik/vlrb/)' používají k jednoznačné identifikaci toho, který VLR je spojen s původním účastníkem (A-strana) a který s příjemcem hovoru (B-strana). Když mobilní účastník zahájí hovor (stane se A-účastníkem), VLR, který aktuálně drží jeho dočasný servisní profil, převezme pro dobu trvání tohoto procesu ustavení a řízení hovoru roli VLRA.

Při nastavování hovoru iniciovaného z mobilní sítě VLRA plní několik klíčových funkcí. Ověřuje, že A-účastníkovi je umožněno hovory iniciovat a že má potřebná předplatitelská práva. Spolupracuje s obsluhujícím [MSC](/mobilnisite/slovnik/msc/) (které se stává MSC-A) k zahájení signalizace pro nastavení hovoru. VLRA poskytuje MSC profil A-účastníka včetně případných služeb kontroly nebo zákazu volání. Pokud jsou pro A-stranu vyvolány služby Camel (Customized Applications for Mobile network Enhanced Logic), hraje VLRA klíčovou roli v aktivování příslušného gsmSCF (uzlu služeb Camel) detekcí nakonfigurovaných spouštěcích bodů v profilu účastníka.

Dále je VLRA ústřední pro procesy účtování. Generuje nebo předává záznamy o účtovaných datech ([CDR](/mobilnisite/slovnik/cdr/)) vztahující se k iniciující větvi hovoru. Tyto záznamy, identifikované rolí VLRA, obsahují podrobnosti jako číslo volajícího, obsluhující MSC, čas začátku a pro pozdější korelaci identifikátor hovoru. Toto rozlišení mezi VLRA a VLRB je zásadní ve složitých scénářích hovorů, například při hovorech mezi dvěma roamujícími účastníky v různých zemích, kde iniciující a koncová síť potřebují jasně identifikovat odpovědné uzly pro řízení služeb, zákonné odposlechy a zúčtování plateb.

## K čemu slouží

Koncept VLRA (a [VLRB](/mobilnisite/slovnik/vlrb/)) byl zaveden, aby poskytl přesné funkční adresování v rámci signalizace a procedur 3GPP. V distribuované síti s miliony scénářů roamingu je prostý identifikátor '[VLR](/mobilnisite/slovnik/vlr/)' nedostatečný k určení, *který* VLR – volajícího nebo volaného – je odkazován v dané zprávě nebo proceduře. Toto rozlišení řeší nejednoznačnost v řízení hovoru, provádění servisní logiky a účtování.

Jeho specifikace byla motivována potřebou jasného a jednoznačného návrhu protokolů, zejména pro pokročilé telefonní služby jako Camel. Camel umožňuje síťovým operátorům definovat vlastní logiku řízení hovoru (např. předplacené služby, virtuální privátní síť). Pro hovor řízený Camel musí síť aktivovat servisní logiku v domovské síti A-účastníka (pomocí VLRA) a potenciálně odlišnou logiku v domovské síti B-účastníka (pomocí VLRB). Bez označení A/B by mohly být signalizační zprávy chápány chybně, což by vedlo k nesprávnému provádění služeb nebo účtování.

Toto funkční rozdělení také řeší požadavky mezifunkčního účtování a zákonného odposlechu. Když jsou do hovoru zapojeni dva různí operátoři (jeden pro volajícího, druhý pro volaného), musí fakturační záznamy jasně přiřazovat poplatky správnému síťovému prvku. Podobně musí být příkazy k odposlechu směrovány na konkrétní VLR (VLRA nebo VLRB) obsluhující cílového účastníka. VLRA je tedy konceptuální nástroj, který přináší přesnost a spolehlivost do víceoperátorské mobilní komunikace obohacené o služby.

## Klíčové vlastnosti

- Logická role přiřazená fyzickému VLR, když jeho obsluhovaný účastník je volající stranou (A-účastník)
- Klíčový uzel pro provádění procedur řízení iniciovaného hovoru a kontrol předplatného
- Aktivuje logiku služeb Camel pro A-stranu na základě detekovaných spouštěcích bodů
- Generuje účtovací data pro iniciující větev hovoru nebo relace
- Identifikován v signalizačních protokolech (např. MAP, CAP) pro správné směrování zpráv
- Nezbytný pro jednoznačnou identifikaci uzlu ve scénářích roamingu mezi více operátory

## Související pojmy

- [VLR – Visitor Location Register](/mobilnisite/slovnik/vlr/)
- [VLRB – Visitor Location Register for the B-subscriber](/mobilnisite/slovnik/vlrb/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)

## Definující specifikace

- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.079** (Rel-19) — Support of Optimal Routeing (SOR) Phase 1

---

📖 **Anglický originál a plná specifikace:** [VLRA na 3GPP Explorer](https://3gpp-explorer.com/glossary/vlra/)
