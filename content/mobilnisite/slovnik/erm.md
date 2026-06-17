---
slug: "erm"
url: "/mobilnisite/slovnik/erm/"
type: "slovnik"
title: "ERM – Eccentric Rotating Mass"
date: 2025-01-01
abbr: "ERM"
fullName: "Eccentric Rotating Mass"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/erm/"
summary: "ERM je typ vibračního aktuátoru používaného v mobilních zařízeních k vytváření haptické zpětné vazby, například pro tiché upozornění a odezvu na dotyk. Definovaný ve specifikacích 3GPP pro testování p"
---

ERM je běžný, cenově výhodný vibrační aktuátor v mobilních zařízeních, který využívá stejnosměrný motor k rotaci vyosené hmoty a vytváří tak haptickou zpětnou vazbu pro upozornění a odezvu na dotyk, jak je definováno ve zkušebních specifikacích 3GPP.

## Popis

Aktuátor s excentrickou rotující hmotou (ERM) je specifická elektromechanická součástka používaná k vytváření vibrací v uživatelském zařízení (UE). Funguje na jednoduchém principu: malý stejnosměrný motor roztáčí nevyváženou hmotu (excentrické závaží) připevněnou k jeho hřídeli. Protože se těžiště hmoty neshoduje s osou rotace, vzniká při rotaci odstředivá síla. Tato síla, která neustále mění směr, jak se hmota otáčí, vede k čistým vibracím, jež jsou přenášeny skrz kryt motoru na pouzdro zařízení. Intenzita vibrací je primárně určena hmotností excentrického závaží, jeho vzdáleností od osy (excentricitou) a rychlostí otáčení (RPM) motoru. Změnou napětí přiváděného na motor se řídí jeho rychlost, což umožňuje modulaci síly vibrací.

V kontextu 3GPP není ERM síťový protokol, ale fyzická součástka zařízení, jejíž charakteristiky jsou odkazovány ve zkušebních specifikacích. Specifikace jako 3GPP TS 27.010 (pro okruhově spínané služby) a TS 26.854 (o haptických kodecích) mohou definovat testovací podmínky nebo zohledňovat přítomnost a vliv vibrací založených na ERM. Například testy výkonu audia nebo přenosu dat mohou potřebovat zohlednit potenciální elektromagnetické rušení nebo fyzické ovlivnění způsobené aktivním vibračním motorem. Klíčovými komponentami systému ERM jsou stejnosměrný motor, excentrická hmota (často poloválcové závaží), ovládací obvod (pro obousměrné řízení se běžně používá H-můstek) a šasi zařízení, které přenáší vibrace na uživatele.

Role ERM ve standardech 3GPP je nepřímá, ale důležitá pro zajištění konzistentního uživatelského zážitku a interoperability zařízení. Zatímco 3GPP nestandardizuje konstrukci aktuátoru jako takovou, uznává běžné implementace v zařízeních. Tím, že zohledňuje vibrace ERM v testovacích plánech, 3GPP zajišťuje, že základní telekomunikační funkce (jako je kvalita hovorového audia nebo integrita dat) nejsou nepříznivě ovlivněny při spuštění haptického upozornění. Navíc, jak se haptická zpětná vazba stává sofistikovanější pro obohacené komunikační služby, pochopení omezení tradiční ERM technologie (jako je pomalá doba odezvy a omezená kontrola tvaru vlny) poskytuje kontext pro vývoj pokročilejších aktuátorů, jako jsou lineární rezonanční aktuátory (LRA), které jsou rovněž pokryty v pozdějších specifikacích.

## K čemu slouží

Účelem odkazování na technologii ERM ve specifikacích 3GPP je zohlednit chování reálných zařízení během testování shody a výkonu. Mobilní zařízení běžně obsahují vibrační motory pro tichá upozornění a ERM byla po léta dominantním, nízkonákladovým řešením. Její činnost může zavádět elektrický šum na napájecích sběrnicích zařízení a vytvářet fyzické mikrofonní efekty, které by potenciálně mohly rušit citlivé audio komponenty nebo vysokofrekvenční obvody. Proto musí zkušební specifikace 3GPP zajistit, že zařízení splňuje všechny standardy kvality komunikace, a to i když je jeho vibrační motor aktivní.

Historicky, jak se mobilní telefony vyvíjely a zahrnovaly vibrační upozornění, byla ERM přímou technologickou volbou. Její zahrnutí do testovacích standardů řeší praktický problém zajištění, že základní funkce zařízení (haptické upozornění) neohrozí primární funkci spolehlivé telekomunikace. Motivací je robustnost na systémové úrovni: operátor sítě potřebuje jistotu, že uživatel přijímající hovor s vibracemi nebude kvůli rušení z motoru zažívat přerušené hovory nebo zhoršenou kvalitu hlasu. Definováním testovacích podmínek, které zahrnují aktivaci ERM, pomáhá 3GPP vytvářet spolehlivý ekosystém, kde pomocné funkce bezproblémově koexistují se základními síťovými službami.

## Klíčové vlastnosti

- Generuje vibrace pomocí odstředivé síly z rotující vyosené hmoty
- Poháněn jednoduchým stejnosměrným motorem s rychlostí řízenou vstupním napětím
- Cenově výhodný a mechanicky jednoduchý design
- Intenzita vibrací je vázána na otáčky motoru (RPM) a vlastnosti hmoty
- Běžně používán pro základní haptiku upozornění a notifikací
- Zohledňován v testech 3GPP pro potenciální rušení komunikačních funkcí

## Definující specifikace

- **TS 26.854** (Rel-19) — Study on Haptics in 5G Media Services
- **TS 27.010** (Rel-19) — Multiplexing Protocol for UE-TE Interface

---

📖 **Anglický originál a plná specifikace:** [ERM na 3GPP Explorer](https://3gpp-explorer.com/glossary/erm/)
