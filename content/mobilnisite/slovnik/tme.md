---
slug: "tme"
url: "/mobilnisite/slovnik/tme/"
type: "slovnik"
title: "TME – Transfer Mode Entity"
date: 2025-01-01
abbr: "TME"
fullName: "Transfer Mode Entity"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tme/"
summary: "Transfer Mode Entity (TME) je entita protokolové vrstvy definovaná v UTRAN specifikacích RRC. Spravuje přenosový režim pro datové přenosy, zajišťuje mapování mezi logickými a transportními kanály a je"
---

TME je protokolová entita RRC v UTRAN, která spravuje přenosové režimy datových přenosů mapováním logických kanálů na transportní kanály za účelem zřizování a rekonfigurace rádiových přenosů v UMTS.

## Popis

Transfer Mode Entity (TME) je funkční komponenta v rámci protokolové vrstvy řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) v UMTS Terrestrial Radio Access Network ([UTRAN](/mobilnisite/slovnik/utran/)), jak je specifikováno ve 3GPP TS 25.331. Funguje jak v uživatelském zařízení (UE), tak v UTRAN (konkrétně v řadiči rádiové sítě, [RNC](/mobilnisite/slovnik/rnc/)). Jejím hlavním úkolem je spravovat konfiguraci přenosového režimu pro rádiové přenosy, což definuje způsob přenosu dat přes rozhraní rádiového rozhraní. TME je zodpovědná za mapování mezi logickými kanály (body přístupu ke službám poskytovanými vrstvou [MAC](/mobilnisite/slovnik/mac/)) a transportními kanály (charakteristiky přenosu dat přes rádiové rozhraní). Toto mapování je základním aspektem procedur zřizování, rekonfigurace a uvolňování rádiových přenosů.

Během zřizování nebo rekonfigurace rádiového přenosu vrstva RRC, využívajíc TME, nakonfiguruje odpovídající přenosový režim na základě požadované kvality služby (QoS). TME zpracovává konfiguraci parametrů, jako je přenosový časový interval ([TTI](/mobilnisite/slovnik/tti/)), kódovací schéma a atributy přizpůsobení přenosové rychlosti. Podporuje různé přenosové režimy, včetně transparentního režimu ([TM](/mobilnisite/slovnik/tm/)), nepotvrzovaného režimu ([UM](/mobilnisite/slovnik/um/)) a potvrzovaného režimu ([AM](/mobilnisite/slovnik/am/)), které odpovídají různým režimům protokolu řízení rádiového spoje (RLC). TME zajišťuje, že nižší vrstvy (RLC a MAC) jsou správně nakonfigurovány pro podporu zvoleného režimu, což přímo ovlivňuje spolehlivost a charakteristiky datového toku.

Fungování TME je úzce provázáno s funkcemi řízení rádiových přenosů. Když se síť rozhodne zřídit nový rádiový přenos pro službu (jako hovor nebo paketovou datovou relaci), vrstva RRC vygeneruje zprávu RADIO BEARER SETUP. Tato zpráva obsahuje konfigurační informace odvozené ze správy TME, které detailně popisují identitu logického kanálu, režim RLC a přidružené parametry transportního kanálu. TME přijímající entity tyto instrukce interpretuje a odpovídajícím způsobem nakonfiguruje své lokální protokolové zásobníky. Tato centralizovaná správa abstrakce přenosového režimu zjednodušuje řídicí logiku a zajišťuje konzistentní konfiguraci mezi UE a sítí pro spolehlivou komunikaci.

## K čemu slouží

TME byla zavedena, aby poskytla strukturovanou a standardizovanou metodu pro správu složitého mapování a konfigurace vyžadované pro přenos dat přes rádiové rozhraní UMTS. Před její formální definicí mohlo být zacházení s mapováním logických na transportní kanály a konfigurace režimu RLC ad-hoc nebo specifické pro implementaci. TME tyto detaily abstrahuje do spravovatelné entity, čímž zjednodušuje řídicí procedury protokolu RRC pro správu rádiových přenosů.

Řeší problém efektivního a spolehlivého zřizování komunikačních kanálů s různorodými požadavky na QoS. Různé služby (např. přepojování okruhů pro hlas, streamované video, prohlížení webu) vyžadují různé přenosové charakteristiky týkající se zpoždění, tolerance chyb a propustnosti. TME poskytuje mechanismus pro převod těchto požadavků služeb na konkrétní, proveditelné konfigurace pro vrstvy RLC a MAC. Její vytvoření bylo motivováno potřebou jasného architektonického oddělení odpovědností v rámci vrstvy RRC, což podporuje interoperabilitu mezi zařízeními od různých výrobců zajištěním společného porozumění a zacházení s konfiguracemi přenosového režimu.

## Klíčové vlastnosti

- Spravuje mapování mezi logickými kanály a transportními kanály
- Konfiguruje režim řízení rádiového spoje (RLC) (transparentní, nepotvrzovaný, potvrzovaný)
- Zpracovává parametry pro přenosový časový interval (TTI) a přizpůsobení přenosové rychlosti
- Nedílná součást procedur zřizování, rekonfigurace a uvolňování rádiových přenosů
- Funguje jak v uživatelském zařízení (UE), tak v řadiči rádiové sítě (RNC)
- Abstrahuje konfigurační detaily nižších vrstev pro řídicí logiku RRC

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)

## Definující specifikace

- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples

---

📖 **Anglický originál a plná specifikace:** [TME na 3GPP Explorer](https://3gpp-explorer.com/glossary/tme/)
