---
slug: "rpg"
url: "/mobilnisite/slovnik/rpg/"
type: "slovnik"
title: "RPG – Role Playing Game"
date: 2025-01-01
abbr: "RPG"
fullName: "Role Playing Game"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rpg/"
summary: "Standardizovaný rámec pro služby her typu role-playing v sítích 3GPP, zavedený ve verzi 16. Definuje síťové schopnosti a rozhraní pro podporu interaktivních víceuživatelských herních zážitků se záruka"
---

RPG je standardizovaný rámec 3GPP, zavedený ve verzi 16, který definuje síťové schopnosti a rozhraní pro podporu interaktivních služeb víceuživatelských her se zárukami kvality služby.

## Popis

Rámec Role Playing Game (RPG) v rámci 3GPP představuje komplexní soubor specifikací navržených k usnadnění působivých víceuživatelských herních služeb přes mobilní sítě. Funguje tak, že definuje standardizovaná rozhraní a síťové funkce, které umožňují herním serverům komunikovat s jádrem sítě 3GPP, konkrétně s 5G Core (5GC). Mezi klíčové architektonické komponenty patří RPG Application Function (RPG-AF), která funguje jako zprostředkovatel mezi herním aplikačním serverem a síťovou funkcí Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)). RPG-AF komunikuje požadavky herní relace – jako je latence, šířka pásma a spolehlivost – směrem k PCF, která je následně převádí na konkrétní pravidla pro řízení politiky a účtování vynucovaná napříč User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) a Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)). Tím je zajištěno, že herní provoz dostává odpovídající zacházení z hlediska Quality of Service (QoS), jako je například prioritní plánování nebo vyhrazené síťové zdroje, pro zachování plynulého uživatelského zážitku.

V jádru rámec RPG využívá možnosti vystavení sítě 3GPP, což umožňuje poskytovatelům herních služeb dynamicky žádat a upravovat síťové zdroje na základě požadavků hry v reálném čase. Například během kritických událostí ve hře vyžadujících ultra-nízkou latenci může RPG-AF aktivovat vytvoření QoS Flow s konkrétními hodnotami 5G QoS Identifier ([5QI](/mobilnisite/slovnik/5qi/)) přizpůsobenými pro interaktivní hraní. Rámec se také zabývá kontinuitou relace a mobilitou, což zajišťuje, že při pohybu uživatele mezi buňkami nebo přístupovými technologiemi si herní relace zachová své výkonnostní charakteristiky bez přerušení. Toho je dosaženo díky těsné integraci s Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) a AMF, které spravují [PDU](/mobilnisite/slovnik/pdu/) relace a události mobility.

Specifikace RPG dále zahrnují aspekty účtování a řízení politik, což operátorům umožňuje monetizovat herní služby prostřednictvím diferencovaných modelů účtování. Rámec podporuje jak online, tak offline systémy účtování, umožňující řízení kreditu v reálném čase nebo účtování po skončení relace na základě délky hraní, spotřeby dat nebo přístupu k prémiovým funkcím. Zohledněna je také bezpečnost, a to mechanismy pro autentizaci herních serverů a ochranu signalizačních zpráv mezi RPG-AF a síťovými funkcemi. Poskytnutím standardizovaného přístupu rámec RPG snižuje fragmentaci, což umožňuje vývojářům her vytvářet konzistentní zážitky napříč různými sítěmi operátorů a zařízeními, a zároveň dává operátorům nástroje pro optimalizaci využití sítě a nabídku herních služeb s přidanou hodnotou.

## K čemu slouží

Rámec RPG byl vytvořen, aby řešil rostoucí poptávku po vysoce kvalitním interaktivním víceuživatelském hraní přes mobilní sítě, kterou tradiční služby internetu typu best-effort nemohly adekvátně podporovat. Před jeho zavedením byl herní provoz zpracováván obecně, což vedlo k problémům, jako je vysoká latence, ztráta paketů a kolísání zpoždění během špičkového zatížení sítě, což výrazně degradovalo zážitek ze hry. Nedostatek standardizovaných rozhraní znamenal, že vývojáři her museli implementovat proprietární řešení nebo spoléhat na obcházení přes [OTT](/mobilnisite/slovnik/ott/) služby, což vedlo k nekonzistentním uživatelským zážitkům a omezené schopnosti operátorů efektivně spravovat síťové zdroje pro hraní.

Podněcováno vzestupem cloudového hraní, esportu a působivých zážitků rozšířené/virtuální reality, 3GPP uznalo potřebu síťově-aware herních služeb. Zaměření verze 16 na vylepšení pro vertikály poskytlo kontext pro definici RPG s cílem využít klíčové schopnosti 5G – jako je síťové dělení, edge computing a ultra-spolehlivá nízkolatenční komunikace ([URLLC](/mobilnisite/slovnik/urllc/)) – konkrétně pro hraní. Rámec řeší problémy jako nepředvídatelný výkon tím, že umožňuje dynamické vyjednávání QoS, což hráčům umožňuje na požádání žádat garantované přenosové rychlosti nebo nízkolatenční cesty. Zabývá se také škálovatelností a monetizací, což operátorům poskytuje standardizovaný způsob, jak vystavit síťové schopnosti poskytovatelům her, a podporuje tak nové obchodní modely, jako jsou prémiová herní předplatná nebo sponzorované datové tarify.

Historicky bylo hraní přes mobilní sítě limitováno nedostatkem koordinace mezi aplikační a síťovou vrstvou. RPG tento rozdíl překlenuje zavedením formalizované architektury, která integruje herní aplikace do ekosystému řízení politik a účtování 3GPP. To nejen zlepšuje technický výkon, ale také podporuje inovace v herních službách, protože vývojáři se mohou spolehnout na konzistentní síťové chování v různých regionech a u různých operátorů. Vytvoření tohoto rámce odráží širší strategii 3GPP podporovat rozmanité průmyslové vertikály pomocí přizpůsobených síťových řešení, což zajišťuje, že potenciál 5G je plně využit pro zábavní aplikace.

## Klíčové vlastnosti

- Dynamické vyjednávání QoS prostřednictvím RPG Application Function (RPG-AF)
- Integrace s funkcí řízení politik 5G Core (PCF) pro vynucování pravidel
- Podpora herních relací s ultra-nízkou latencí a vysokou spolehlivostí
- Schopnosti účtování a fakturace pro monetizaci herních služeb
- Správa mobility a kontinuity relace během hraní
- Vystavení sítě pro žádosti o zdroje ze strany serverů her třetích stran

## Definující specifikace

- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services

---

📖 **Anglický originál a plná specifikace:** [RPG na 3GPP Explorer](https://3gpp-explorer.com/glossary/rpg/)
