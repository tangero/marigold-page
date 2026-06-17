---
slug: "must"
url: "/mobilnisite/slovnik/must/"
type: "slovnik"
title: "MUST – Multiuser Superposition Transmission"
date: 2025-01-01
abbr: "MUST"
fullName: "Multiuser Superposition Transmission"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/must/"
summary: "Technika neortogonálního vícečetného přístupu (NOMA), při níž jsou signály pro více uživatelů superponovány a přenášeny na stejném časově-frekvenčním zdroji s různými úrovněmi výkonu. Zvyšuje spektrál"
---

MUST je neortogonální technika vícečetného přístupu, při níž jsou signály pro více uživatelů superponovány na stejném časově-frekvenčním zdroji s různými úrovněmi výkonu za účelem zvýšení spektrální účinnosti a uživatelské kapacity.

## Popis

Multiuser Superposition Transmission (MUST) je downlinkový přenosový schéma fyzické vrstvy standardizované v 3GPP pro LTE a studované pro NR. Jedná se o formu neortogonálního vícečetného přístupu (NOMA), při níž základnová stanice ([eNB](/mobilnisite/slovnik/enb/) nebo gNB) vysílá složený signál superpozicí modulovaných symbolů určených pro více uživatelů na stejný blok fyzického zdroje (PRB) v časové a frekvenční doméně. Superpozice je dosaženo přidělením různých úrovní výkonu signálu každého uživatele. Typicky je uživateli v centru buňky (s dobrými podmínkami kanálu) přidělen nižší výkon, zatímco uživateli na okraji buňky (se špatnými podmínkami kanálu) je přidělen vyšší výkon. Složený signál je vysílán všesměrově a každý uživatel na straně přijímače využívá postupnou interferenční korekci (SIC) k dekódování zamýšlené informace.

Architektura MUST zahrnuje vylepšení plánovače a řetězce zpracování fyzického downlinkového sdíleného kanálu ([PDSCH](/mobilnisite/slovnik/pdsch/)). Plánovač spáruje uživatele s výrazně odlišnými zisky kanálu (např. s různou vzdáleností od základnové stanice) pro superpozici na stejných zdrojích. Určuje poměr přidělení výkonu mezi spárovanými uživateli. Vysílač pak provádí superpozici konstelací, při níž jsou konstelace pro vzdáleného a blízkého uživatele zkombinovány do nové, hustší konstelační mapy pro přenos. Klíčové komponenty zahrnují algoritmus párování uživatelů pro MUST, regulátor přidělování výkonu a generování mapování superponované konstelace, které musí být přijímačům známo nebo signalizováno pro úspěšné SIC.

Na straně přijímače blízký uživatel (s lepším kanálem) nejprve dekóduje signál vzdáleného uživatele tím, že vlastní signál považuje za šum, a to díky vyššímu přidělení výkonu signálu vzdáleného uživatele. Po úspěšném dekódování a rekonstrukci signálu vzdáleného uživatele jej blízký uživatel odečte (zruší) z přijatého složeného signálu. Následně dekóduje vlastní signál z čistšího zbylého signálu. Vzdálený uživatel se svým horším kanálem jednoduše dekóduje vlastní signál přímo, přičemž signál blízkého uživatele s nižším výkonem považuje za dodatečný šum, který má kvůli rozdílu ve výkonu minimální dopad. Tento proces umožňuje oběma uživatelům sdílet stejné rádiové zdroje, čímž se ve srovnání s tradičními ortogonálními technikami vícečetného přístupu ([OMA](/mobilnisite/slovnik/oma/)), jako je [OFDMA](/mobilnisite/slovnik/ofdma/), zvyšuje celková spektrální účinnost a kapacita systému.

## K čemu slouží

MUST byl vyvinut pro řešení stále rostoucí poptávky po vyšší spektrální účinnosti a uživatelské kapacitě v celulárních sítích, zejména s exponenciálním růstem datového provozu. Tradiční ortogonální schémata vícečetného přístupu, jako je [OFDMA](/mobilnisite/slovnik/ofdma/) používané v LTE, přidělují každému uživateli exkluzivní časově-frekvenční zdroje, aby se předešlo interferenci. Zatímco to zjednodušuje návrh přijímače, omezuje to počet současně obsluhovaných uživatelů, zejména v hustých scénářích. Motivací pro MUST byla potřeba překonat tuto ortogonální bariéru a obsloužit více uživatelů ve stejném pásmu, což je koncept ústřední pro NOMA.

Historický kontext pro zavedení MUST v 3GPP Release 14 představoval průzkum technik NOMA v odvětví jako klíčového kandidáta pro 5G. Raný výzkum ukázal významný potenciální zisk v propustnosti a konektivitě. MUST konkrétně cílil na vylepšení sítí LTE zpětně kompatibilním způsobem a poskytnutí plynulé evoluční cesty. Zaměřoval se na scénáře s různorodými podmínkami kanálu uživatelů, jako je mix uživatelů v centru a na okraji buňky, kde je superpozice ve výkonové doméně nejúčinnější. Tím, že umožňuje těmto uživatelům sdílet zdroje, MUST zlepšuje spravedlnost a propustnost na okraji buňky, což jsou kritické metriky pro uživatelský zážitek.

Dále MUST řeší omezení čistě ortogonálního plánování při zvládání masivní konektivity, což je požadavek pro internet věcí (IoT). Zatímco jeho primární studium probíhalo v LTE, jeho principy ovlivnily diskuse o NOMA pro NR. Tato technologie řeší problém nedostatku zdrojů využitím výkonové domény jako dodatečného rozměru multiplexování. Její vznik byl hnán potřebou efektivnějšího využití licencovaného spektra s konečným cílem poskytnout vyšší datové rychlosti a podpořit více souběžných uživatelů bez nutnosti dodatečné šířky pásma, což je pro operátory vzácný a drahý zdroj.

## Klíčové vlastnosti

- Neortogonální sdílení zdrojů prostřednictvím superpozice ve výkonové doméně
- Párování uživatelů na základě rozdílu zisku kanálu (např. blízcí-vzdálení uživatelé)
- Adaptivní přidělování výkonu mezi spárované uživatele
- Postupná interferenční korekce (SIC) na straně přijímače
- Superpozice konstelací a mapování pro složený přenos
- Lze integrovat s existujícími plánovači OFDMA pro hybridní přístup

## Související pojmy

- [OMA – Open Mobile Alliance](/mobilnisite/slovnik/oma/)
- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)
- [OFDMA – Orthogonal Frequency Division Multiple Access](/mobilnisite/slovnik/ofdma/)

## Definující specifikace

- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [MUST na 3GPP Explorer](https://3gpp-explorer.com/glossary/must/)
