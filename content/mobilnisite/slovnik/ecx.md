---
slug: "ecx"
url: "/mobilnisite/slovnik/ecx/"
type: "slovnik"
title: "ECx – Error Condition for static C/I conditions with C/I = x dB"
date: 2025-01-01
abbr: "ECx"
fullName: "Error Condition for static C/I conditions with C/I = x dB"
category: "Physical Layer"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/ecx/"
summary: "ECx odkazuje na standardizovanou chybovou podmínku definovanou ve specifikacích 3GPP pro testování výkonu přijímače za statických podmínek poměru nosná/interference (C/I) při konkrétní hodnotě x dB. P"
---

ECx je standardizovaná chybová podmínka pro testování výkonu přijímače za statických podmínek poměru nosná/interference při konkrétní hodnotě x dB, používaná v 3GPP testech shody.

## Popis

ECx je testovací podmínka specifikovaná v technických specifikacích 3GPP pro testování rádiové frekvence ([RF](/mobilnisite/slovnik/rf/)) shody uživatelského zařízení (UE). Definuje statický scénář, ve kterém je poměr nosná/interference ([C/I](/mobilnisite/slovnik/c-i/)) nastaven na pevnou hodnotu x decibelů (dB), přičemž x je parametr, jako například 0, 3 nebo 6 dB, jak je definováno v testovacích případech. Tato podmínka se používá k vyhodnocení schopnosti přijímače správně demodulovat a dekódovat signály za přítomnosti konstantní úrovně ko-kanálové nebo přilehlé kanálové interference, čímž simuluje reálné scénáře, kde interference omezuje výkon.

Architektura pro testování ECx zahrnuje testovací systém skládající se z generátorů signálu pro požadovaný a rušivý signál, simulátoru útlumu pro emulaci podmínek rádiového kanálu (ačkoli statické C/I znamená žádný útlum na aspektu interference) a testovaného UE. Požadovaný signál představuje přenos obslužné buňky, zatímco rušivý signál napodobuje nežádoucí signál z jiného zdroje na určité úrovni výkonu vůči nosné, čímž je dosaženo cílového poměru C/I. Za těchto řízených podmínek se provádějí měření pro posouzení chybovosti, jako je například bloková chybovost ([BLER](/mobilnisite/slovnik/bler/)) nebo rámcová chybovost ([FER](/mobilnisite/slovnik/fer/)), aby se ověřilo, že UE splňuje minimální výkonnostní standardy.

Klíčové komponenty zahrnují schopnost testovacího zařízení přesně řídit úrovně výkonu a parametry modulace, stejně jako definici referenčních měřicích kanálů ([RMC](/mobilnisite/slovnik/rmc/)) a testovacích modelů. Podmínky ECx se uplatňují v různých testovacích sadách, včetně správy rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)) a požadavků na RF, což zajišťuje, že zařízení mohou udržet konektivitu a propustnost v prostředích omezených interferencí. Její role je klíčová pro certifikaci, že UE poskytují spolehlivý provoz v různých nasazeních sítí, zejména v hustých městských oblastech, kde je interference běžná. Statická povaha zjednodušuje opakovatelnost a srovnávací testy, čímž vytváří základnu pro složitější testy s dynamickou interferencí.

## K čemu slouží

ECx bylo zavedeno za účelem standardizace testování přijímače za řízených interferenčních podmínek, čímž reaguje na potřebu konzistentních výkonnostních měřítek napříč různými modely UE a výrobci. Před formalizací takových podmínek 3GPP se testovací metodologie lišily, což vedlo k možným nesrovnalostem ve výkonu zařízení a problémům s interoperabilitou v živých sítích. Definováním konkrétních poměrů [C/I](/mobilnisite/slovnik/c-i/) umožňuje ECx objektivní vyhodnocení odolnosti UE vůči interferenci, což je nezbytné pro zajištění kvality služby v celulárních sítích, kde je spektrum sdílené a interference je limitujícím faktorem.

K jeho vytvoření motivoval vývoj mobilních systémů směrem k vyšší spektrální efektivitě a hustším sítím, počínaje Release 8 a LTE. Jelikož se sítě stávaly více omezenými interferencí kvůli opětovnému využití frekvencí a koexistenci více technologií, stalo se nezbytným ověřit, že zařízení mohou spolehlivě fungovat na hranici pokrytí nebo ve scénářích s vysokou interferencí. ECx řeší problém kvantifikace citlivosti přijímače za přítomnosti interference, což pomáhá udržovat výkon sítě a uživatelský zážitek. Poskytuje základní testovací případ pro shodu a přijetí operátorem, což zajišťuje, že zařízení splňují minimální provozní standardy před nasazením.

## Klíčové vlastnosti

- Definice statického poměru nosná/interference (C/I) pro testování
- Aplikace v testovacích případech RF shody a výkonu
- Vyhodnocení chybovosti, jako je BLER, za řízené interference
- Využití referenčních měřicích kanálů a testovacích modelů
- Podpora různých kmitočtových pásem a síťových technologií (např. LTE, NR)
- Umožňuje srovnávací testy citlivosti přijímače a potlačení interference

## Definující specifikace

- **TS 26.077** (Rel-19) — AMR Noise Suppression Minimum Performance Requirements

---

📖 **Anglický originál a plná specifikace:** [ECx na 3GPP Explorer](https://3gpp-explorer.com/glossary/ecx/)
