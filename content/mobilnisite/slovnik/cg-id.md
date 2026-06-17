---
slug: "cg-id"
url: "/mobilnisite/slovnik/cg-id/"
type: "slovnik"
title: "CG-ID – Character Group Identifier"
date: 2025-01-01
abbr: "CG-ID"
fullName: "Character Group Identifier"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cg-id/"
summary: "CG-ID je kód používaný v sítích 3GPP k identifikaci konkrétní znakové skupiny pro službu Cell Broadcast Service (CBS). Umožňuje síti cílit vysílané zprávy na konkrétní geografické oblasti nebo skupiny"
---

CG-ID je kód používaný v sítích 3GPP k identifikaci konkrétní znakové skupiny pro službu Cell Broadcast Service, což umožňuje cílení zpráv na geografické oblasti nebo skupiny uživatelů.

## Popis

Identifikátor znakové skupiny (Character Group Identifier, CG-ID) je základní parametr v architektuře služby Cell Broadcast Service ([CBS](/mobilnisite/slovnik/cbs/)) dle 3GPP, standardizovaný v TS 23.042. Funguje jako jedinečný kód identifikující konkrétní 'znakovou skupinu', což je v podstatě logické seskupení informací určených k vysílání. CG-ID je klíčovou součástí identifikátoru zprávy Cell Broadcast Message Identifier ([CBMI](/mobilnisite/slovnik/cbmi/)), což je 16bitová hodnota. CBMI je strukturován tak, aby obsahoval jak identifikátor zprávy (Message ID), tak CG-ID. Konkrétní přidělení bitů pro CG-ID v rámci CBMI může být definováno sítí, což umožňuje flexibilitu v tom, kolik bitů je vyhrazeno pro identifikaci znakové skupiny oproti konkrétní zprávě. Tato struktura umožňuje, aby byla jedna vysílaná zpráva asociována s konkrétní znakovou skupinou.

Provozně se CG-ID používá v Cell Broadcast Centre ([CBC](/mobilnisite/slovnik/cbc/)), síťové entitě odpovědné za vytváření a plánování vysílaných zpráv. Když CBC připraví zprávu k distribuci, přiřadí jí CBMI obsahující příslušný CG-ID. Tento CBMI spolu s obsahem zprávy a informacemi pro geografické cílení (jako seznam cílových Cell ID) je odeslán k řadičům základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) v sítích 2G nebo k řadičům rádiové sítě (RNC) v sítích 3G UMTS. Tyto uzly RAN následně instruují příslušné základnové stanice ([BTS](/mobilnisite/slovnik/bts/) nebo NodeB), aby zprávu vysílaly přes rozhraní vzduch na kanálu Cell Broadcast Channel ([CBCH](/mobilnisite/slovnik/cbch/)).

Na straně uživatelského zařízení (UE) toto zařízení nepřetržitě monitoruje CBCH. Po přijetí vysílané zprávy UE extrahuje CBMI. Firmware nebo software zařízení následně zpracuje část CG-ID. Primární funkcí pro UE je filtrování. UE může být nakonfigurováno (často uživatelem nebo operátorem sítě) tak, aby přijímalo a zobrazovalo zprávy pouze z určitých znakových skupin. Například UE může být nastaveno tak, aby upozorňovalo uživatele pouze na zprávy s CG-ID odpovídajícím 'Systému varování před zemětřesením a tsunami' nebo 'Komerčním službám a reklamám'. Zprávy patřící k nevybraným znakovým skupinám jsou typicky potichu zahazovány UE, čímž se zabrání obtěžování uživatele nerelevantními vysíláními. Toto cílené filtrování je klíčové pro použitelnost CBS, zejména proto, že služba může být využita pro širokou škálu typů informací, od kritických veřejných varování po méně naléhavé komerční nebo dopravní aktualizace.

Role CG-ID přesahuje pouhé filtrování zpráv. Je nedílnou součástí schopnosti CBS současně vysílat více nezávislých informačních proudů. Použitím různých CG-ID může síť současně vysílat varování před počasím, kurzy akcií a nouzová varování na stejném fyzickém kanálu. RAN vysílá všechny zprávy, ale filtrační mechanismus UE založený na CG-ID prezentuje koncovému uživateli pouze relevantní podmnožinu. Tato architektura zajišťuje efektivní využití vysílacích rádiových zdrojů a zároveň poskytuje personalizovaný a zvládnutelný uživatelský zážitek. Definice a správa číselného prostoru CG-ID jsou typicky odpovědností operátora sítě nebo národních regulačních orgánů, zejména pro standardizované systémy veřejného varování.

## K čemu slouží

CG-ID byl vytvořen, aby řešil základní výzvu kategorizace zpráv a uživatelem volitelného filtrování v rámci jednosměrné vysílací služby, jako je [CBS](/mobilnisite/slovnik/cbs/). Před jeho standardizací vysílací systémy často postrádaly detailní mechanismus k rozlišení mezi různými typy vysílaného obsahu. Bez takového identifikátoru by mobilní zařízení muselo uživateli zobrazovat každou jednu vysílanou zprávu, což by vedlo k informačnímu přetížení a potenciálně by uživatele vedlo k úplnému vypnutí služby, což by bylo katastrofální pro systémy veřejného varování.

Zavedení CG-ID jako součásti [CBMI](/mobilnisite/slovnik/cbmi/) ve 3GPP Release 99 poskytlo strukturované řešení. Vyřešilo problém diferenciace služeb. Tím, že umožnilo označit každou vysílanou zprávu identifikátorem skupiny, mohla síť nabízet více logických 'kanálů' informací na jediném fyzickém vysílacím kanálu. To umožnilo komerční životaschopnost CBS mimo nouzová varování a umožnilo informační služby založené na předplatném (např. zprávy, sportovní výsledky, lokalizovaná reklama) bez narušení kritické funkce varování před katastrofami.

CG-ID navíc posílil koncového uživatele. Přesunul kontrolu na zařízení, což uživatelům umožnilo přihlásit se pouze ke kategoriím informací, které považovali za hodnotné. Toto uživatelsky orientované řešení bylo klíčové pro přijetí služby. Pro operátory sítí a úřady poskytl CG-ID standardizovaný, škálovatelný rámec pro správu různorodých vysílacích služeb, přidělování číselných rozsahů pro konkrétní účely (např. rezervace určitých hodnot CG-ID pro národní nouzová varování) a zajištění, že kritické zprávy mohou být přesně cíleny a identifikovány kompatibilními zařízeními, čímž se plní regulační požadavky na systémy veřejného varování.

## Klíčové vlastnosti

- Umožňuje logickou kategorizaci zpráv Cell Broadcast Service do odlišných skupin neboli 'kanálů'
- Tvoří nedílnou součnost 16bitového identifikátoru zprávy Cell Broadcast Message Identifier (CBMI)
- Umožňuje uživatelskému zařízení filtrovat a zobrazovat pouze zprávy z uživatelem vybraných znakových skupin
- Podporuje současné vysílání více nezávislých informačních služeb na jediném fyzickém kanálu
- Usnadňuje cílené šíření zpráv pro systémy veřejného varování a služby založené na poloze
- Poskytuje škálovatelný rámec pro operátory sítí ke správě různorodých nabídek vysílacích služeb

## Definující specifikace

- **TS 23.042** (Rel-19) — Data Compression and Decompression for 3GPP

---

📖 **Anglický originál a plná specifikace:** [CG-ID na 3GPP Explorer](https://3gpp-explorer.com/glossary/cg-id/)
