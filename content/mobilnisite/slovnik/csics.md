---
slug: "csics"
url: "/mobilnisite/slovnik/csics/"
type: "slovnik"
title: "CSICS – Circuit Switched IMS Combinational Service"
date: 2025-01-01
abbr: "CSICS"
fullName: "Circuit Switched IMS Combinational Service"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/csics/"
summary: "CSICS umožňuje současné využívání hlasových hovorů v přepojování okruhů a multimediálních služeb založených na IMS prostřednictvím jediného rádiového spojení. Operátorům umožňuje nabízet rozšířené slu"
---

CSICS je technologie 3GPP, která umožňuje současné využívání hlasových hovorů v přepojování okruhů a multimediálních služeb založených na IMS prostřednictvím jediného rádiového spojení, čímž propojuje starší a IP sítě.

## Popis

Circuit Switched IMS Combinational Service (CSICS) je standardizovaná architektura 3GPP, která umožňuje současný provoz hlasových hovorů v přepojování okruhů ([CS](/mobilnisite/slovnik/cs/)) a multimediálních relací IP Multimedia Subsystem (IMS) přes stejné rádiové spojení. Technologie funguje tak, že prostřednictvím tradičních mobilních ústředen ([MSC](/mobilnisite/slovnik/msc/)) naváže hlasový hovor v CS, zatímco současně přes paketově přepínanou doménu zřídí multimediální relaci založenou na IMS. Tento dvoudoménový provoz umožňuje uživatelům udržet kvalitní hlasový hovor a zároveň využívat doplňkové služby IMS, jako je sdílení videa, přenos souborů nebo informace o stavu.

Z architektonického hlediska CSICS zahrnuje koordinaci mezi více síťovými prvky včetně mobilní ústředny (MSC), [SGSN](/mobilnisite/slovnik/sgsn/), GGSN a prvků jádra IMS, jako je [CSCF](/mobilnisite/slovnik/cscf/) a aplikační servery. MSC zpracovává hlasovou cestu v přepojování okruhů, zatímco jádro IMS spravuje zřizování a řízení multimediální relace. Klíčovou součástí je [SCC](/mobilnisite/slovnik/scc/) [AS](/mobilnisite/slovnik/as/), který koordinuje domény CS a IMS, aby zajistil kontinuitu služeb a správnou synchronizaci mezi oběma relacemi.

Technologie funguje prostřednictvím specifických signalizačních procedur definovaných ve specifikacích 3GPP. Když uživatel zahájí hlasový hovor v CS, síť může současně aktivovat zřizování IMS relace pomocí signalizace [SIP](/mobilnisite/slovnik/sip/). UE udržuje dva samostatné přenašeče: jeden pro hlasový provoz CS a druhý pro multimediální provoz IMS. Přístupová síť musí podporovat souběžné přenašeče CS a [PS](/mobilnisite/slovnik/ps/), čehož je dosaženo mechanismy jako je DTM v GERAN nebo současný provoz CS a PS v UTRAN. Synchronizace mezi hlasovou a multimediální složkou je řízena pomocí časových referencí a protokolů pro koordinaci relací.

CSICS hraje klíčovou roli ve vývoji sítí tím, že umožňuje operátorům zavádět služby založené na IMS bez nutnosti okamžité migrace na plná nasazení VoLTE nebo VoNR. Poskytuje přechodové řešení, které využívá stávající infrastrukturu CS a zároveň umožňuje nové multimediální služby. Technologie podporuje různé kombinace služeb včetně hlasu CS se sdílením videa založeným na IMS, hlasu CS s instant messagingem založeným na IMS a hlasu CS s přenosem souborů založeným na IMS, čímž vytváří obohacené komunikační zážitky při zachování spolehlivé kvality hlasové služby.

## K čemu slouží

CSICS byl vyvinut k řešení výzvy zavádění multimediálních služeb založených na IMS při zachování kompatibility se stávajícími hlasovými sítěmi s přepojováním okruhů. Když mobilní operátoři začali nasazovat infrastrukturu IMS ve verzi 7, čelili dilematu, zda čekat na plné nasazení VoLTE, nebo najít mezilehlé řešení, které by mohlo okamžitě poskytovat rozšířené služby. CSICS poskytl tento most tím, že umožnil operátorům nabízet multimediální služby IMS souběžně s tradičními hlasovými hovory v CS, což umožnilo rychlejší uvedení obohacených komunikačních služeb na trh.

Technologie řešila několik konkrétních problémů: Za prvé řešila omezení pokrytí raných paketově přepínaných sítí využitím všudypřítomného pokrytí hlasových sítí CS. Za druhé umožnila poskytovatelům služeb dříve zhodnotit své investice do IMS nabídkou služeb s přidanou hodnotou bez nutnosti kompletní přestavby sítě. Za třetí poskytla uživatelům obohacené komunikační zážitky při zachování spolehlivosti a kvality tradičních hlasových hovorů. To bylo obzvláště důležité během přechodného období, kdy se kvalita a pokrytí hlasu v paketově přepínaných sítích stále vyvíjely.

Historicky se CSICS objevil v období, kdy mobilní sítě přecházely z čistě okruhově přepínaných architektur na plně IP sítě. Předchozí přístupy vyžadovaly samostatné relace pro hlasové a multimediální služby, což bylo neefektivní a poskytovalo špatný uživatelský zážitek. CSICS zavedl koncept kombinačních služeb, kde mohly být hlasové a multimediální složky synchronizovány a prezentovány uživateli jako jednotná služba. Tím řešil omezení starších technologií, jako je okruhově přepínaná videotelefonie, která vyžadovala vyhrazené kanály a nabízela omezenou flexibilitu ve srovnání s multimediálními službami založenými na IMS.

## Klíčové vlastnosti

- Současné zřizování hlasové relace CS a multimediální relace IMS
- Zpětná kompatibilita se staršími sítěmi s přepojováním okruhů
- Synchronizace mezi hlasovou a multimediální složkou
- Podpora různých kombinací služeb (sdílení videa, přenos souborů, zasílání zpráv)
- Využití stávajícího pokrytí CS pro spolehlivou hlasovou službu
- Přechodová architektura umožňující zavádění služeb IMS

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 22.279** (Rel-19) — CS and IMS Combinational Services Requirements
- **TR 22.979** (Rel-19) — CS-IMS Combinational Service Requirements
- **TS 24.279** (Rel-19) — Combined CS Calls and IMS Sessions
- **TS 24.879** (Rel-7) — CS and IMS Service Combination

---

📖 **Anglický originál a plná specifikace:** [CSICS na 3GPP Explorer](https://3gpp-explorer.com/glossary/csics/)
