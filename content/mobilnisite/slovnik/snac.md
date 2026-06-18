---
slug: "snac"
url: "/mobilnisite/slovnik/snac/"
type: "slovnik"
title: "SNAC – Shared Network Area Code"
date: 2025-01-01
abbr: "SNAC"
fullName: "Shared Network Area Code"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/snac/"
summary: "Identifikátor používaný v UMTS k jednoznačnému definování sdílené síťové oblasti v rámci PLMN. Umožňuje operátorům sdílet síťovou infrastrukturu při zachování oddělených core sítí a správy účastníků."
---

SNAC (Shared Network Area Code) je identifikátor v UMTS, který jednoznačně definuje sdílenou síťovou oblast v rámci PLMN a umožňuje sdílení infrastruktury mezi operátory, zatímco si zachovávají oddělené core sítě a správu účastníků.

## Popis

Shared Network Area Code (SNAC) je klíčový identifikátor v architektuře UMTS, specificky definovaný v protokolu Radio Access Network Application Part ([RANAP](/mobilnisite/slovnik/ranap/)) podle 3GPP TS 25.413. Působí v kontextu sdílené sítě, což je scénář, kdy více operátorů Public Land Mobile Network ([PLMN](/mobilnisite/slovnik/plmn/)) využívá společnou infrastrukturu radio access network (RAN), jako jsou Node B a Radio Network Controllers ([RNC](/mobilnisite/slovnik/rnc/)), ale udržují nezávislé core network (CN) elementy jako Mobile Switching Centers ([MSC](/mobilnisite/slovnik/msc/)) a Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Nodes ([SGSN](/mobilnisite/slovnik/sgsn/)). Primární funkcí SNAC je poskytnout jednoznačnou identifikaci konkrétní sdílené síťové oblasti, což je geografický region obsluhovaný sdíleným RAN.

Z architektonické perspektivy RNC používá SNAC ke směrování signalizace a uživatelských dat ke správnému uzlu core sítě operátora. Když User Equipment (UE) iniciuje spojení ve sdílené síťové oblasti, RNC přijme International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)) nebo Temporary Mobile Subscriber Identity ([TMSI](/mobilnisite/slovnik/tmsi/)) UE. RNC pomocí konfiguračního mapování, často založeného na části Mobile Network Code (MNC) z IMSI nebo jiné směrovací informaci, určí příslušného operátora core sítě. SNAC je pak zahrnut v relevantních RANAP zprávách, jako je Initial UE Message nebo Relocation Required message, aby informoval core síť o konkrétní sdílené oblasti, ze které spojení pochází. To umožňuje uzlu core sítě aplikovat správné účastnické politiky, pravidla účtování a procedury mobility management specifické pro tuto sdílenou oblast.

Zpracování protokolu zahrnuje SNAC jako parametr v rámci informačních elementů RANAP. Zajišťuje, že během procedur jako handover, paging nebo location updating může síť správně asociovat aktivitu UE s doménou správného operátora ve sdílené infrastruktuře. Bez SNAC by mohla vzniknout nejednoznačnost vedoucí k chybám směrování, neúspěšným handoverům nebo nesprávnému poskytování služeb. Proto je SNAC základním prvkem pro praktickou implementaci modelů sdílení sítí specifikovaných 3GPP, jako je Multi-Operator Core Network (MOCN) a Gateway Core Network (GWCN), což umožňuje technickou a komerční spolupráci mezi operátory.

## K čemu slouží

SNAC byl vytvořen k řešení technických výzev sdílení infrastruktury mezi operátory mobilních sítí. Před jeho specifikací každý operátor typicky nasazoval svůj vlastní exkluzivní RAN a CN. Jak se spektrum a získávání lokalit stávaly dražšími a regulační tlaky na pokrytí rostly, operátoři hledali způsoby, jak snížit kapitálové a provozní výdaje prostřednictvím sdílení. Původní přístupy postrádaly standardizovanou metodu, jak může RAN jednoznačně identifikovat a směrovat provoz do více core sítí přes stejnou fyzickou infrastrukturu.

Zavedení SNAC ve Release 5 poskytlo tento standardizovaný identifikátor. Vyřešil problém jednoznačné identifikace oblasti v rámci sdíleného RAN, což je zásadní pro výběr core sítě, zákonné odposlechy, účtování a mobility management. Například během handoveru z nesdílené oblasti do sdílené oblasti potřebuje cílový RNC signalizovat správnému operátorovi core sítě, která konkrétní sdílená oblast je zapojena. SNAC poskytuje tuto kritickou informaci, zajišťuje plynulou kontinuitu služeb a správnou administrativní segregaci mezi partnery ve sdílení. Jeho vytvoření bylo motivováno posunem průmyslu ke sdílení sítí jako strategickému nástroji pro rychlé nasazení, zejména pro 3G/UMTS sítě, a pro poskytování pokrytí ve venkovských nebo náročných oblastech, kde individuální nasazení sítě nebylo ekonomicky životaschopné.

## Klíčové vlastnosti

- Jednoznačně identifikuje sdílenou síťovou oblast v rámci PLMN
- Umožňuje správné směrování signalizace a uživatelských dat k příslušnému operátorovi core sítě ve scénáři se sdíleným RAN
- Parametr v rámci protokolu RANAP (Radio Access Network Application Part)
- Nezbytný pro procedury mobility jako handover a relocation ve sdílených sítích
- Podporuje architektury sdílení sítí jako MOCN (Multi-Operator Core Network)
- Usnadňuje oddělený provoz a údržbu pro každého operátora ve sdílené oblasti

## Související pojmy

- [RANAP – Radio Access Network Application Protocol](/mobilnisite/slovnik/ranap/)
- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)
- [MOCN – Multiple Operator Core Network](/mobilnisite/slovnik/mocn/)
- [RNC – Radio Network Controller](/mobilnisite/slovnik/rnc/)

## Definující specifikace

- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)

---

📖 **Anglický originál a plná specifikace:** [SNAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/snac/)
