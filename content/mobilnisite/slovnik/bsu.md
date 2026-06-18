---
slug: "bsu"
url: "/mobilnisite/slovnik/bsu/"
type: "slovnik"
title: "BSU – Broadcast Service User"
date: 2025-01-01
abbr: "BSU"
fullName: "Broadcast Service User"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bsu/"
summary: "Broadcast Service User (BSU) je logická entita představující uživatele nebo zařízení, které využívá vysílací/skupinové služby v sítích 3GPP. Je to klíčový koncept v architektuře Multimedia Broadcast M"
---

BSU je logická entita představující uživatele nebo zařízení, které využívá vysílací (broadcast) nebo skupinové (multicast) služby v sítích 3GPP, a která funguje jako koncový bod pro doručování obsahu v architektuře MBMS.

## Popis

Broadcast Service User (BSU) je základní logická entita v rámci architektury Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) konsorcia 3GPP, standardizovaná primárně v TS 22.947. Představuje koncového spotřebitele služeb pro doručování vysílacího a skupinového obsahu. Na rozdíl od tradičního uživatele s individuálním přenosem (unicast) je BSU definován předplatným a spotřebou jedné či více služeb MBMS, což může zahrnovat mobilní [TV](/mobilnisite/slovnik/tv/), aktualizace softwaru, nouzová upozornění nebo živé přenosy událostí. Koncept BSU abstrahuje fyzické uživatelské zařízení (UE) a zaměřuje se na vztah spotřeby služby, což síti umožňuje spravovat vysílací relace, uplatňovat politiky specifické pro službu a provádět přesné účtování na základě využití služby, nikoli jednotlivých toků paketů.

Architektonicky existuje BSU ve vrstvě služeb architektury MBMS. Interaguje s Broadcast-Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)), což je vstupní bod pro poskytovatele obsahu a který spravuje relace MBMS. BM-SC provádí autentizaci a autorizaci BSU pro konkrétní služby, často s využitím profilu předplatného uživatele uloženého v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). Když BSU aktivuje službu MBMS, síť vytvoří kontext přenosu (bearer context), který zahrnuje identitu BSU, požadovanou službu a přidružené parametry QoS. Tento kontext je propagován napříč základní sítí (přes MBMS Gateway a Mobility Management Entity) a rádiovou přístupovou sítí (přes eNodeB v LTE nebo gNB v 5G NR), aby bylo zajištěno efektivní doručování obsahu všem předplatným BSU v cílové oblasti.

Role BSU je klíčová pro několik síťových funkcí. Pro správu služeb umožňuje identita BSU síti sledovat, kteří uživatelé přijímají které vysílací toky, což umožňuje dynamickou správu relací (jako spouštění/ukončování toků na základě poptávky). Pro účtování poskytuje BSU logický bod pro uplatňování účtovacích modelů specifických pro vysílání, které se mohou lišit od modelů pro individuální přenos (např. paušální, událostní nebo časové účtování). Z hlediska QoS určuje profil služby BSU prioritu, šířku pásma a toleranci chyb pro doručování obsahu MBMS, čímž zajišťuje konzistentní uživatelský zážitek. V 5G se tento koncept vyvíjí spolu se službami enhanced Mobile Broadband (eMBB) a multicast-broadcast, kde mohou BSU plynule přepínat mezi režimy individuálního a vysílacího přenosu na základě síťových podmínek a požadavků služby.

Operačně je BSU typicky asociován s dočasným kontextem přenosu MBMS během aktivní relace služby. BSU může být identifikován pomocí dočasného identifikátoru, jako je [TMGI](/mobilnisite/slovnik/tmgi/) (Temporary Mobile Group Identity), v kombinaci s uživatelskými přihlašovacími údaji. Síť monitoruje aktivitu BSU za účelem optimalizace využití prostředků – například, pokud v určité buňce není předplacen žádný BSU, může síť v této buňce vysílání pozastavit, aby šetřila rádiové prostředky. Koncept BSU také podporuje mobilitu: když se uživatel pohybuje, jeho kontext BSU je aktualizován, aby bylo zajištěno nepřetržité přijímání služby napříč různými oblastmi vysílací služby, což je řízeno procedurami jako je kontinuita služby MBMS.

## K čemu slouží

Koncept Broadcast Service User (BSU) byl zaveden, aby řešil jedinečné požadavky vysílacích a skupinových služeb v celulárních sítích, které se zásadně liší od tradičních individuálních (unicast) služeb typu bod-bod. Před [MBMS](/mobilnisite/slovnik/mbms/) a abstrakcí BSU se sítě 3GPP primárně zaměřovaly na individuální komunikaci, kde měl každý uživatel vyhrazené spojení. Tento přístup byl neefektivní pro doručování populárního obsahu (jako živé sportovní přenosy nebo zprávy) mnoha uživatelům současně, protože duplikoval datové toky a spotřebovával nadměrné síťové prostředky. BSU poskytuje standardizovaný způsob, jak modelovat uživatele jako spotřebitele sdílených vysílacích toků, což umožňuje efektivní doručování typu jeden-všem a řeší výzvy škálovatelnosti individuálního přenosu pro hromadnou distribuci obsahu.

Historicky motivace pro BSU vznikla s vývojem MBMS v 3GPP Release 6, jehož cílem byla podpora mobilní [TV](/mobilnisite/slovnik/tv/) a skupinové komunikace. Formalizace BSU v Release 9 (jak je dokumentováno v TS 22.947) však upřesnila architektonický model jasným oddělením uživatele služby od podkladových transportních mechanismů. Toto oddělení umožnilo operátorům spravovat vysílací služby nezávisle na technologiích rádiového přístupu (např. přechod z 3G na LTE a později na vysílání v 5G). Abstrakce BSU také řešila obchodní potřeby tím, že umožnila flexibilní poskytování služeb – operátoři mohli nabízet vysílací balíčky založené na předplatném, zkušební služby nebo volně přijímatelný obsah, přičemž vše bylo sledováno prostřednictvím identit BSU pro účtování a analytiku.

Koncept BSU dále řeší technická omezení související s povědomím o službě a optimalizací sítě. Bez definované entity BSU by síť zacházela s vysílacími pakety jako s anonymními datagramy, což by ztěžovalo implementaci uživatelsky specifických politik, jako jsou rodičovské kontroly pro mobilní TV nebo cílená nouzová upozornění. Modelováním BSU standardy 3GPP umožňují inteligenci na vrstvě služeb: síť může autentizovat uživatele pro prémiový obsah, monitorovat využití služby pro zajištění kvality a dynamicky přidělovat prostředky na základě počtu a rozložení aktivních BSU. Tento účel pokračuje i v aplikacích éry 5G, jako jsou komunikace pro veřejnou bezpečnost, aktualizace v automobilovém průmyslu a imerzivní média, kde je efektivní skupinové doručování identifikovaným skupinám uživatelů nezbytné.

## Klíčové vlastnosti

- Logická reprezentace spotřebitele vysílací/skupinové služby
- Umožňuje službě specifickou autentizaci a autorizaci prostřednictvím BM-SC
- Podporuje flexibilní modely účtování pro doručování vysílacího obsahu
- Umožňuje správu QoS a vynucování politik pro toky MBMS
- Umožňuje dynamickou správu relací na základě přítomnosti aktivních uživatelů
- Poskytuje podporu mobility pro nepřetržité přijímání vysílací služby

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [TMGI – Temporary Multicast Group Identifier](/mobilnisite/slovnik/tmgi/)

## Definující specifikace

- **TR 22.947** (Rel-19) — Personal Broadcast Service (PBS) Use Cases

---

📖 **Anglický originál a plná specifikace:** [BSU na 3GPP Explorer](https://3gpp-explorer.com/glossary/bsu/)
