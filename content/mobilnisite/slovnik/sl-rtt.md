---
slug: "sl-rtt"
url: "/mobilnisite/slovnik/sl-rtt/"
type: "slovnik"
title: "SL-RTT – Sidelink Round Trip Time"
date: 2025-01-01
abbr: "SL-RTT"
fullName: "Sidelink Round Trip Time"
category: "Radio Access Network"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/sl-rtt/"
summary: "Přímá metoda měření vzdálenosti a určování polohy mezi zařízeními. Měří celkovou dobu, za kterou signál přenese z jednoho UE k druhému a zpět. To umožňuje dvěma UE vypočítat vzdálenost mezi sebou bez"
---

SL-RTT je přímá metoda měření vzdálenosti mezi zařízeními (device-to-device), která měří celkovou dobu šíření signálu z jednoho UE k druhému a zpět, což umožňuje dvěma UE vypočítat vzdálenost mezi sebou.

## Popis

Sidelink Round Trip Time (SL-RTT) je technika měření vzdálenosti a určování polohy standardizovaná pro 3GPP sidelink komunikaci. Jedná se o obousměrné měření doby letu (time-of-flight) prováděné přímo mezi dvěma uživatelskými zařízeními (UE) přes rozhraní PC5. Na rozdíl od metod založených na časovém rozdílu je SL-RTT metoda měření vzdálenosti (ranging), která měří absolutní zpoždění šíření mezi dvojicí zařízení. Procedura zahrnuje iniciující UE a odpovídající UE. Iniciující UE vysílá specifický signál pro měření vzdálenosti, často Sidelink Positioning Reference Signal ([SL-PRS](/mobilnisite/slovnik/sl-prs/)), a zaznamená čas odeslání (T1). Odpovídající UE tento signál přijme, zaznamená jeho čas příjmu a po známém, pevném zpracovacím zpoždění vysílá zpět odpovědní signál k iniciátorovi. Iniciující UE přijme tuto odpověď a zaznamená čas jejího příjmu (T4). Doba oběhu (round-trip time) se vypočítá jako (T4 - T1) mínus známé zpracovací zpoždění na straně odpovídajícího zařízení. Vzdálenost mezi dvěma UE se pak odvodí jako ([RTT](/mobilnisite/slovnik/rtt/) * rychlost světla) / 2. Klíčovou výhodou této metody je, že nevyžaduje těsnou časovou synchronizaci mezi dvěma UE, protože měření je uzavřeno v rámci hodin iniciátora. Architektura zahrnuje přesný návrh signálů na fyzické vrstvě pro měřící signály, procedury řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) pro koordinaci výměny měření a protokoly pro hlášení výsledků. SL-RTT může být použita jako samostatná metoda měření vzdálenosti mezi dvěma zařízeními nebo kombinována s měřeními úhlu příchodu (AoA) nebo s více SL-RTT měřeními mezi několika zařízeními pro určení relativní nebo absolutní polohy v síti.

## K čemu slouží

SL-RTT byl vyvinut, aby poskytl jednoduchou, robustní a přesnou metodu pro přímé měření vzdálenosti mezi dvěma sidelink zařízeními. Řeší potřebu peer-to-peer měření vzdálenosti v aplikacích, jako je detekce blízkosti, jemně odstupňované relativní určování polohy pro zabránění kolizím a zabezpečené párování zařízení. Předchozí metody často vyžadovaly asistenci sítě nebo vysoce synchronizované hodiny, což není vždy dostupné nebo praktické v čistě device-to-device scénářích, zejména pro komunikace v oblasti veřejné bezpečnosti nebo [V2X](/mobilnisite/slovnik/v2x/) mimo pokrytí sítě. SL-RTT řeší problém synchronizace hodin použitím obousměrného měření, které eliminuje časový posun mezi lokálními hodiny obou zařízení. To jej činí velmi vhodným pro ad-hoc nasazení a nasazení bez infrastruktury. Jeho vytvoření bylo motivováno požadavky pokročilých V2X služeb, jako je kooperativní vnímání, kde vozidla potřebují znát přesnou vzdálenost k blízkým vozidlům nebo zranitelným účastníkům silničního provozu, a průmyslových IoT aplikací vyžadujících přesné sledování aktiv prostřednictvím přímé komunikace zařízení.

## Klíčové vlastnosti

- Poskytuje přímé měření vzdálenosti mezi dvěma UE bez nutnosti časové synchronizace.
- Je založena na principu obousměrného měření doby letu (ToF).
- Využívá Sidelink Positioning Reference Signals (SL-PRS) pro výměnu při měření vzdálenosti.
- Vnitřně kompenzuje časové posuny mezi iniciujícím a odpovídajícím UE.
- Podporuje jak měření vzdálenosti, tak určování polohy při kombinaci s jinými měřeními.
- Je definována s konkrétními sekvencemi zpráv a časovými omezeními pro zajištění přesnosti.

## Související pojmy

- [SL-PRS – Sidelink Positioning Reference Signals](/mobilnisite/slovnik/sl-prs/)
- [SL-RTOA – Sidelink Relative Time of Arrival](/mobilnisite/slovnik/sl-rtoa/)

## Definující specifikace

- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.355** (Rel-19) — Sidelink Positioning Protocol (SLPP)

---

📖 **Anglický originál a plná specifikace:** [SL-RTT na 3GPP Explorer](https://3gpp-explorer.com/glossary/sl-rtt/)
