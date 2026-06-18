---
slug: "uus1"
url: "/mobilnisite/slovnik/uus1/"
type: "slovnik"
title: "UUS1 – User-to-User Signalling Service 1"
date: 2025-01-01
abbr: "UUS1"
fullName: "User-to-User Signalling Service 1"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/uus1/"
summary: "Komponenta doplňkové služby UUS, která volajícímu uživateli umožňuje odeslat informace volanému uživateli během fáze zřizování hovoru. Data jsou přenášena uvnitř počáteční zprávy SETUP od volajícího a"
---

UUS1 je doplňková služba, která volajícímu uživateli umožňuje odeslat informace volanému uživateli uvnitř zprávy pro zřízení hovoru před jeho přijetím.

## Popis

User-to-User Signalling Service 1 (UUS1) je jedna ze tří specifických služeb tvořících širší doplňkovou službu [UUS](/mobilnisite/slovnik/uus/) v sítích 3GPP. Je definována jako služba asociovaná s hovorem, kde přenos uživatelských informací iniciuje volající strana a probíhá během pokusu o zřízení hovoru. Technicky terminálové zařízení volajícího uživatele zahrne informační prvek User-to-User (UUIE) do zprávy SETUP odeslané síti na začátku hovoru. Síť po přijetí této zprávy SETUP zkontroluje, zda má volající předplacenu službu UUS1, a pokud je autorizován, transparentně přepošle tento informační prvek v následující zprávě [ISUP](/mobilnisite/slovnik/isup/) Initial Address Message ([IAM](/mobilnisite/slovnik/iam/)) směrem k cílové síti.

Přijímající síť po provedení vlastní kontroly služby pro volanou stranu (pokud to vyžaduje síťová politika) doručí UUIE volanému terminálu, typicky uvnitř zprávy SETUP prezentované volanému uživateli. To umožňuje, aby informace byly k dispozici na volaném zařízení před přijetím hovoru. Obsah UUIE není standardizován 3GPP a je určen pro interpretaci na aplikační vrstvě; může se jednat o textový řetězec, číselný kód nebo jiná data do maximální povolené délky. Služba je striktně určena pro přenos informací od volajícího k volanému během zřizování; v rámci fáze zřizování hovoru není definováno žádné potvrzení nebo odpověď přes UUS1.

Architektonicky UUS1 spoléhá na funkce řízení hovoru v [MSC](/mobilnisite/slovnik/msc/) nebo obsluhující ústředně pro zpracování UUIE. [HLR](/mobilnisite/slovnik/hlr/) ukládá profil služeb UUS účastníka, který udává, zda je UUS1 povolena. Během zřizování hovoru může MSC tento profil dotazovat přes [MAP](/mobilnisite/slovnik/map/) nebo použít lokálně uložená data. Zpracování protokolu zahrnuje vložení UUIE do pole Discriminátoru protokolu a polí specifických pro typ zprávy v [DSS1](/mobilnisite/slovnik/dss1/) (na rozhraní uživatel-síť) a do parametru User-to-User ve zprávách ISUP (uvnitř páteřní sítě). Pokud se hovor nezřídí (např. obsazeno, neozvání se), data UUS1 jsou typicky zahozena, protože jejich přenos je podmíněn pokračováním procesu zřizování hovoru.

## K čemu slouží

UUS1 byla navržena k řešení specifického problému jednosměrného přenosu dat iniciovaného volající stranou na samém začátku pokusu o hovor. Před její existencí neměla volající strana standardizovaný způsob, jak odeslat kontextové informace (jako účel hovoru, identifikační kód nebo značku priority) spolu se samotným zřizováním hovoru. To bylo zvláště užitečné pro automatizované systémy, telemetrii nebo obchodní aplikace, kde volané zařízení mohlo přijatá data použít k rozhodnutí, jak hovor zpracovat (např. směrovat na konkrétního agenta, zobrazit kontext volajícího nebo spustit automatizovanou odpověď).

Odstranila omezení starších systémů, kde musel být takový kontext sdělen verbálně po přijetí hovoru nebo přes samostatný kanál, což přidávalo zpoždění a složitost. Integrací dat do počáteční zprávy SETUP umožnila UUS1 rychlejší zpracování a inteligentnější obsluhu hovoru v místě příchodu. Její úspěch však byl limitován potřebou podpory funkce na obou koncových bodech a ve všech mezilehlých sítích a byla z velké části nahrazena bohatší signalizací založenou na [SIP](/mobilnisite/slovnik/sip/) v VoIP sítích.

## Klíčové vlastnosti

- Přenos uživatelských informací iniciovaný volající stranou během fáze zřizování hovoru
- Uživatelská data jsou přenášena uvnitř počáteční zprávy SETUP a odpovídající zprávy IAM
- Umožňuje doručení dat volané straně před přijetím hovoru
- Vyžaduje předplacení služby pro volající stranu
- Transparentní síťový přenos s ověřením předplatného
- Maximální délka uživatelských dat definována omezeními sítě a protokolu (typicky až 128 oktetů)

## Související pojmy

- [UUS – User-to-User Signalling Supplementary Service](/mobilnisite/slovnik/uus/)
- [UUS2 – User-to-User Signalling Service 2](/mobilnisite/slovnik/uus2/)
- [IAM – Initial Address Message](/mobilnisite/slovnik/iam/)

## Definující specifikace

- **TS 23.087** (Rel-19) — User-to-User Signalling (UUS) Stage 2
- **TS 24.087** (Rel-19) — User-to-User Signalling (UUS) Stage 3

---

📖 **Anglický originál a plná specifikace:** [UUS1 na 3GPP Explorer](https://3gpp-explorer.com/glossary/uus1/)
