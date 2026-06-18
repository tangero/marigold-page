---
slug: "gstn"
url: "/mobilnisite/slovnik/gstn/"
type: "slovnik"
title: "GSTN – General Switched Telephone Network"
date: 2025-01-01
abbr: "GSTN"
fullName: "General Switched Telephone Network"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/gstn/"
summary: "Tradiční veřejná telefonní síť s komutací okruhů (PSTN), která poskytuje základní telefonní službu (POTS). V kontextu 3GPP představuje starší (legacy) telefonní síť, se kterou musí mobilní sítě spolup"
---

GSTN je tradiční veřejná telefonní síť s komutací okruhů (PSTN), se kterou mobilní sítě spolupracují, aby zajistily kontinuitu hlasových hovorů a doplňkové služby.

## Popis

General Switched Telephone Network (GSTN) označuje globální, vzájemně propojený celek veřejných telefonních sítí s komutací okruhů, běžně známý jako Public Switched Telephone Network ([PSTN](/mobilnisite/slovnik/pstn/)). Ve specifikacích 3GPP, zejména těch souvisejících s architekturou jádra sítě a spoluprácí sítě (např. TS 24.229 pro protokoly IP Multimedia Subsystem), se termín GSTN používá pro označení této starší (legacy) telefonní infrastruktury. Jedná se o síť s komutací okruhů, kde je na dobu trvání hlasového hovoru mezi dvěma stranami vytvořen vyhrazený fyzický nebo logický spoj („okruh“). Síť se skládá z ústředen (jako ústředny třídy 4 a třídy 5), přenosových tras (měděné, optické) a signalizačních systémů (primárně signalizační systém č. 7 – [SS7](/mobilnisite/slovnik/ss7/)).

Z architektonického hlediska GSTN funguje na principu časového multiplexu ([TDM](/mobilnisite/slovnik/tdm/)) pro hlasové kanály. Každému hlasovému hovoru je přidělen konkrétní časový slot v digitálním proudu, což poskytuje předvídatelnou službu s konstantní přenosovou rychlostí. Mezi klíčové komponenty patří místní ústředny (připojující účastnické linky), tranzitní ústředny (pro směrování hovorů mezi ústřednami) a mezinárodní brány. Řídicí rovinu zajišťuje síť SS7, která využívá samostatné signalizační kanály k navázání, správě a ukončení hovorů a k poskytování služeb, jako je identifikace volajícího nebo přesměrování hovoru. Toto oddělení hlasové a signalizační cesty je charakteristickým rysem architektury GSTN.

V kontextu systémů 3GPP je GSTN externí síť, se kterou musí jádro mobilní sítě spolupracovat. Tato spolupráce je klíčová pro poskytování hlasových hovorů mezi mobilními účastníky a účastníky pevné linky v PSTN. V jádrech 2G/3G s komutací okruhů toho bylo dosaženo prostřednictvím Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)). Ve 4G a 5G, kde je jádro sítě paketově orientované (založené na IP), tuto funkci spolupráce zajišťují specifické uzly. Pro hlasové služby založené na IMS (VoLTE, VoNR) s GSTN komunikují funkce Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)) a IMS Media Gateway ([IM-MGW](/mobilnisite/slovnik/im-mgw/)). MGCF překládá signalizaci [SIP](/mobilnisite/slovnik/sip/) z IMS do zpráv [ISUP](/mobilnisite/slovnik/isup/) pro síť SS7, zatímco IM-MGW provádí konverzi mezi médii založenými na IP (RTP) a médii založenými na TDM. To umožňuje bezproblémovou kontinuitu hlasových služeb mezi paketově orientovaným mobilním světem a starším světem s komutací okruhů.

## K čemu slouží

GSTN existuje jako historický základ globální telefonie a poskytuje již více než století všudypřítomnou, spolehlivou a kvalitní hlasovou komunikaci. Jejím účelem v ekosystému 3GPP je zajistit zpětnou kompatibilitu a kontinuitu služeb. Když byly poprvé nasazeny mobilní sítě, jejich primární službou byla mobilní telefonie a potřebovaly se připojit k rozsáhlé stávající základně účastníků pevných linek a služeb v PSTN. GSTN představovala zavedený standard, ke kterému se musely mobilní sítě připojit.

Tvorba a vývoj standardů 3GPP musely s touto starší infrastrukturou počítat. Problém, který řeší, je vzájemné propojení: bez definovaných postupů spolupráce by byly mobilní sítě izolovanými ostrovy. Motivací pro specifikaci spolupráce s GSTN ve standardech, jako je TS 24.229, bylo zaručit, že hovor z 5G smartphonu může dosáhnout telefonu pevné linky a naopak, a to s řádným překladem signalizace a konverzí médií. Tím se řeší omezení nových síťových technologií fungujících ve vakuu; musí se integrovat s již nasazenou základnou. Jak se sítě vyvíjejí směrem k plně IP, GSTN představuje starší doménu, která je postupně nahrazována, ale během přechodného období zůstává kriticky důležitá.

## Klíčové vlastnosti

- Architektura s komutací okruhů s vyhrazeným spojením pro každý hovor
- Pro hlasové kanály používá časový multiplex (TDM)
- Pro mimopásmovou signalizaci a řízení hovorů spoléhá na signalizační systém č. 7 (SS7)
- Poskytuje vysokou spolehlivost a kvalitu hlasu (POTS)
- Globálně propojená a standardizovaná pro mezinárodní volání
- Podporuje základní doplňkové služby (čekání na lince, přesměrování hovoru atd.)

## Související pojmy

- [PSTN – Public Switched Telecommunications Network](/mobilnisite/slovnik/pstn/)
- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)
- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)
- [IM-MGW – IP Multimedia Media Gateway Function](/mobilnisite/slovnik/im-mgw/)

## Definující specifikace

- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP

---

📖 **Anglický originál a plná specifikace:** [GSTN na 3GPP Explorer](https://3gpp-explorer.com/glossary/gstn/)
