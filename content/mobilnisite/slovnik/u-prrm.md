---
slug: "u-prrm"
url: "/mobilnisite/slovnik/u-prrm/"
type: "slovnik"
title: "U-PRRM – UTRAN Position Radio Resource Management"
date: 2025-01-01
abbr: "U-PRRM"
fullName: "UTRAN Position Radio Resource Management"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/u-prrm/"
summary: "Funkce UTRAN odpovědná za správu a přidělování rádiových prostředků speciálně využívaných pro polohovací činnosti. Zajišťuje, aby polohovací procedury měly potřebnou šířku pásma, časové sloty a signal"
---

U-PRRM je funkce UTRAN, která spravuje a přiděluje rádiové prostředky speciálně vyžadované pro polohovací procedury, a zajišťuje, aby měly potřebnou kapacitu bez zhoršení běžných komunikačních služeb.

## Popis

Funkce [UTRAN](/mobilnisite/slovnik/utran/) Position Radio Resource Management (U-PRRM) je specializovaný správce prostředků v rámci polohovací architektury UTRAN, typicky implementovaný v řadiči rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)). Jejím účelem je přidělování a dohled nad rádiovými prostředky vyhrazenými pro polohovací operace. Když [U-PRCF](/mobilnisite/slovnik/u-prcf/) koordinuje polohovací proceduru (např. [OTDOA](/mobilnisite/slovnik/otdoa/) relaci vyžadující přenos referenčních signálů z více buněk), konzultuje s U-PRRM, aby zajistil potřebné prostředky. U-PRRM rozhoduje o tom, které bloky fyzických prostředků, časové sloty nebo kódy mohou být použity pro polohovací referenční signály ([PRS](/mobilnisite/slovnik/prs/)). Spravuje kompromis mezi přesností určování polohy (která může vyžadovat více prostředků) a dopadem na kapacitu pro datový provoz uživatelů. Funkce řeší potenciální konflikty, například když se překrývají žádosti o polohovací prostředky od více uživatelských zařízení (UE) nebo služeb. Také spravuje prostředky pro polohovací signalizaci, jako jsou zprávy příkazů k měření a hlášení na vyhrazených nebo společných kanálech. Díky vyhrazené entitě [RRM](/mobilnisite/slovnik/rrm/) pro určování polohy může síť implementovat sofistikované politiky – například upřednostňovat žádosti o nouzové určení polohy před komerčními [LBS](/mobilnisite/slovnik/lbs/) žádostmi nebo dynamicky upravovat přidělování polohovacích prostředků na základě celkového vytížení buňky.

## K čemu slouží

U-PRRM byl zaveden, aby vyřešil kritický problém soupeření o rádiové prostředky mezi polohovacími službami a konvenčními hlasovými/datovými službami v [UTRAN](/mobilnisite/slovnik/utran/). Polohovací činnosti, zejména metody jako OTDOA, které vyžadují periodický přenos referenčních signálů z více buněk, spotřebovávají cenné rádiové prostředky (výkon, šířku pásma, kódy). Bez vyhrazeného řízení by tyto činnosti mohly nekontrolovaně zhoršit kapacitu sítě a kvalitu služeb pro ostatní uživatele. U-PRRM poskytuje řízený, na politice založený mechanismus pro přidělování prostředků speciálně pro určování polohy. Tím je zajištěno, že polohovací služby, zejména povinné nouzové služby, mohou mít garantovány potřebné prostředky pro splnění požadavků na přesnost a latenci, a zároveň je minimalizován negativní dopad na celkový výkon sítě. Jeho vznik odráží vývoj mobilních sítí na víceúčelové platformy, kde musí být správa prostředků detailní a vědomá si služeb. Řeší omezení dřívějších, monolitičtějších přístupů RRM, které nebyly navrženy pro zvládnutí specifických, periodických a na měření náročných požadavků pokročilých polohovacích technologií.

## Klíčové vlastnosti

- Přiděluje a spravuje rádiové prostředky (např. výkon, časové sloty, kódy) pro polohovací signály a procedury
- Zajišťuje plánování prostředků pro vysílání polohovacích referenčních signálů (PRS) v OTDOA
- Spravuje prostředky pro polohovací signalizační kanály a hlášení měření
- Implementuje na politice založenou prioritu (např. nouzové vs. komerční polohovací žádosti)
- Optimalizuje využití prostředků k vyvážení přesnosti určování polohy s celkovou kapacitou provozu v buňce
- Komunikuje s U-PRCF, aby schválila nebo zamítla žádosti o prostředky pro konkrétní polohovací relace

## Související pojmy

- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)
- [RNC – Radio Network Controller](/mobilnisite/slovnik/rnc/)
- [U-PRCF – UTRAN Position Radio Co-ordination Function](/mobilnisite/slovnik/u-prcf/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)

## Definující specifikace

- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [U-PRRM na 3GPP Explorer](https://3gpp-explorer.com/glossary/u-prrm/)
