---
slug: "ntsc"
url: "/mobilnisite/slovnik/ntsc/"
type: "slovnik"
title: "NTSC – National Time Service Center of Chinese Academy of Sciences"
date: 2025-01-01
abbr: "NTSC"
fullName: "National Time Service Center of Chinese Academy of Sciences"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ntsc/"
summary: "Národní instituce pro udržování času v Číně, která poskytuje autoritativní reference koordinovaného světového času (UTC). Ve standardech 3GPP je uváděna jako potenciální zdroj důvěryhodného času pro s"
---

NTSC je Národní časový servisní středisko (National Time Service Center) Čínské akademie věd, národní instituce pro udržování času, která poskytuje autoritativní reference UTC pro potenciální použití při synchronizaci sítí 3GPP.

## Popis

Národní časové servisní středisko (NTSC) Čínské akademie věd je čínským národním úřadem pro časové služby, odpovědným za generování, udržování a distribuci národního standardního času [UTC](/mobilnisite/slovnik/utc/)(NTSC), který je sladěn s koordinovaným světovým časem (UTC). V kontextu specifikací 3GPP je NTSC uznáváno jako příklad důvěryhodného externího časového zdroje. Telekomunikační sítě vyžadují vysoce přesné a spolehlivé časové reference pro různé funkce, včetně synchronizace základnových stanic, časového značkování síťových událostí a podpory bezpečnostních protokolů, jako je bezpečná distribuce času pro zákonné odposlechy.

V architektuře 3GPP může funkce distribuce času ([TDF](/mobilnisite/slovnik/tdf/)) sítě získat čas UTC z externího zdroje, jako je NTSC. TDF by se typicky připojovala k časovým distribučním službám NTSC, které mohou využívat metody jako Network Time Protocol ([NTP](/mobilnisite/slovnik/ntp/)), Precision Time Protocol ([PTP](/mobilnisite/slovnik/ptp/)) nebo satelitní signály. Získaný čas je pak považován za důvěryhodný, protože pochází z národního metrologického institutu. Specifikace 3GPP, jako jsou specifikace pro LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) v TS 36.355 a jeho protějšky, mohou odkazovat na NTSC jako na entitu poskytující pomocná časová data nebo jako na příklad spolehlivého časového serveru.

Úlohou NTSC v síťovém ekosystému je fungovat jako primární časový zdroj stratum-1. Integrita jeho časového signálu a zpětná vysledovatelnost k mezinárodním standardům jsou klíčové. Pro síťové operátory, zejména v Číně, zajišťuje používání NTSC jako časového zdroje soulad s národními předpisy a poskytuje společnou časovou základnu. To je nezbytné pro synchronizaci systémů s časovým duplexním dělením ([TDD](/mobilnisite/slovnik/tdd/)), koordinaci předávání hovorů a zajištění přesnosti a právní obhajovatelnosti časových značek pro bezpečnostní události a zákonné odposlechy. Odkaz na NTSC v dokumentech 3GPP poskytuje konkrétní reálný příklad toho, jak se sítě mohou propojit s národními časovými úřady, aby dosáhly bezpečné synchronizace.

## K čemu slouží

Zařazení a uznání NTSC ve specifikacích 3GPP slouží k poskytnutí standardizovaného odkazu na důvěryhodný časový úřad na národní úrovni. Tím se řeší problém závislosti sítí na libovolných nebo neověřených časových zdrojích, což by mohlo vést k chybám synchronizace, bezpečnostním slabinám a nesouladu s právními požadavky na časové značkování odposlechnutých komunikací. Historicky sítě mohly používat různé komerční nebo méně vysledovatelné servery [NTP](/mobilnisite/slovnik/ntp/), kterým chyběla záruka metrologické vysledovatelnosti.

Motivace vychází z potřeby interoperability a souladu s předpisy, zejména v regionech s přísnými národními standardy. Specifikací entity jako je NTSC poskytuje 3GPP model pro integraci síťového zařízení s oficiálními časovými službami. To je obzvláště důležité pro funkce jako určování polohy (kde je pro [OTDOA](/mobilnisite/slovnik/otdoa/) zapotřebí přesný čas), bezpečná distribuce času (NTP-UTC) a provoz sítě v regulovaných trzích. Odkazování na NTSC pomáhá výrobcům zařízení a operátorům navrhovat systémy, které se mohou připojit k podobným národním časovým službám po celém světě, a zajišťuje tak konzistentní přístup k získávání důvěryhodného času. Řeší to omezení spočívající v absenci standardizovaného odkazu na to, co představuje 'důvěryhodný externí časový zdroj' v nasazovacích scénářích.

## Klíčové vlastnosti

- Národní úřad pro generování a udržování UTC(NTSC)
- Poskytuje vysledovatelné časové reference sladěné s mezinárodními standardy
- Distribuuje čas pomocí více metod (např. NTP, PTP, satelitní signály)
- Ve specifikacích 3GPP je uváděno jako důvěryhodný externí časový zdroj pro synchronizaci sítě
- Podporuje právní a regulatorní požadavky na přesné časové značkování
- Umožňuje synchronizaci sítě pro provoz TDD a polohové služby

## Související pojmy

- [UTC – Coordinated Universal Time](/mobilnisite/slovnik/utc/)

## Definující specifikace

- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 44.031** (Rel-19) — Radio Resource LCS Protocol (RRLP)

---

📖 **Anglický originál a plná specifikace:** [NTSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ntsc/)
