---
slug: "ipd"
url: "/mobilnisite/slovnik/ipd/"
type: "slovnik"
title: "IPD – Integrated Passive Device"
date: 2025-01-01
abbr: "IPD"
fullName: "Integrated Passive Device"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ipd/"
summary: "Integrated Passive Device (IPD) je miniaturní elektronická součástka, která integruje více pasivních prvků (rezistory, kondenzátory, cívky) do jednoho povrchově montovatelného pouzdra pomocí tenkovrst"
---

IPD je miniaturní elektronická součástka, která integruje více pasivních prvků do jednoho pouzdra pro kompaktní RF front-end moduly v mobilních zařízeních.

## Popis

Integrated Passive Device (IPD) je specializovaný typ součástky vyráběný procesy podobnými integrovaným obvodům ([IC](/mobilnisite/slovnik/ic/)), ale navržený k vytváření vysokovýkonných pasivních sítí namísto aktivních tranzistorů. Na rozdíl od diskrétních rezistorů, kondenzátorů a cívek pájených jednotlivě na DPS integruje IPD tyto prvky na jediný substrát – často křemík, sklo nebo specializovaný laminát s nízkými ztrátami – pomocí fotolitografie a tenkovrstvého nanášení. Tím vzniká monolitická síť s přesně definovanými elektrickými charakteristikami a extrémně malými rozměry.

Architektonicky se IPD skládá z strukturovaných vodivých vrstev (pro cívky a propojení), dielektrických vrstev (pro kondenzátory) a odporových filmů. Cívky s vysokým činitelem jakosti (Q) jsou vytvářeny pomocí spirálových nebo meandrových vzorů. Kondenzátory jsou tvořeny pomocí paralelních desek nebo struktur kov-izolant-kov ([MIM](/mobilnisite/slovnik/mim/)). Rezistory jsou vyrobeny z tenkých filmů materiálů, jako je nitrid tantalu nebo nikl-chrom. Klíčovou výhodou je schopnost vytvářet složité [LC](/mobilnisite/slovnik/lc/) (cívka-kondenzátor) nebo [RLC](/mobilnisite/slovnik/rlc/) (rezistor-cívka-kondenzátor) sítě s úzkými tolerancemi, vynikající reprodukovatelností a minimálními parazitními jevy díky kontrolovanému výrobnímu prostředí a miniaturním propojení.

V kontextu 3GPP a návrhu mobilních zařízení jsou IPD nepostradatelné v radiofrekvenčním ([RF](/mobilnisite/slovnik/rf/)) front-endu (RFFE). Plní několik kritických funkcí. Za prvé, pro ladění antén: moderní smartphony podporují širokou škálu kmitočtových pásem (od sub-1 GHz po mmWave). Jedna anténa nemůže být optimálně účinná ve všech pásmech. Ladící obvody na bázi IPD (sítě přepínaných kondenzátorů a cívek) jsou umístěny mezi anténu a transceiver, aby dynamicky upravovaly impedanci antény a maximalizovaly účinnost vyzařování pro právě aktivní pásmo. Za druhé, pro impedanční přizpůsobení: poskytují přesné přizpůsobovací sítě mezi výkonovými zesilovači ([PA](/mobilnisite/slovnik/pa/)), filtry (jako BAW/SAW), přepínači a anténou, aby zajistily maximální přenos výkonu a minimalizovaly odraz signálu ([VSWR](/mobilnisite/slovnik/vswr/)). Za třetí, používají se k vytváření kompaktních symetrizačních členů (transformátorů symetrický-nesymetrický) a rozdělovačů/kombinátorů výkonu pro [MIMO](/mobilnisite/slovnik/mimo/) a diverzitní anténní cesty. Nakonec mohou IPD implementovat jednoduché filtrační funkce nebo sloužit jako blokování stejnosměrného proudu a RF drossle. Jejich integrace šetří cennou plochu DPS, snižuje počet součástek, zlepšuje spolehlivost a zvyšuje celkový RF výkon u vícepásmových a vícemódových zařízení.

## K čemu slouží

Vývoj a přijetí IPD bylo hnací silou neustálé miniaturizace a požadavků na výkon spotřební elektroniky, zejména smartphonů. Jak se buněčné standardy vyvíjely od 2G k 5G, počet potřebných RF komponent (filtrů, přepínačů, zesilovačů) explodoval kvůli agregaci nosných, MIMO a novým kmitočtovým pásmům. Používání diskrétních pasivních součástek pro každou přizpůsobovací síť, filtr a ladící obvod se stalo fyzicky nemožným v rámci zmenšujících se rozměrů moderních zařízení. Diskrétní součástky také trpí parazitními jevy na vysokých kmitočtech (zejména mmWave), nižší reprodukovatelností a vyššími náklady na montáž.

IPD tyto problémy řeší tím, že nabízejí vysoce integrovanou, přesnou alternativu. Byly vytvořeny ke konsolidaci 'moře pasivních prvků', které obklopovaly každou aktivní RF součástku. Monolitickou integrací těchto sítí dosahují konstruktéři několika klíčových výhod: drastického snížení nároků na plochu součástky na DPS, zlepšení elektrického výkonu díky kontrolovaným parazitním jevům a vyšším činitelům Q pro cívky, zvýšené spolehlivosti díky menšímu počtu pájecích spojů a nižším celkovým nákladům na montáž. Pro 3GPP je umožnění pokročilých funkcí, jako je agregace nosných (CA) a 4x4 MIMO v elegantních designech telefonů, přímo závislé na takových integračních technologiích. IPD spolu s dalšími integrovanými moduly (jako PAMiD – moduly výkonového zesilovače s integrovanými duplexery) jsou tím, co činí současné vícegigabitové 5G smartphony praktickou realitou.

## Klíčové vlastnosti

- Monolitická integrace rezistorů, kondenzátorů a cívek na jediném substrátu
- Extrémně malé rozměry a povrchově montovatelné pouzdro (např. 01005, 0201)
- Vysoký činitel jakosti (Q) pro cívky a kondenzátory, klíčový pro RF výkon
- Přesné hodnoty součástek a úzké tolerance díky polovodičové výrobě
- Nízká parazitní indukčnost a kapacita díky miniaturním propojením
- Umožňuje složité RF sítě, jako jsou impedanční ladící obvody, symetrizační členy a rozdělovače výkonu

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TR 26.905** (Rel-19) — Study on Mobile 3D Video Services
- **TR 38.820** (Rel-16) — NR; 7-24 GHz Frequency Range Study

---

📖 **Anglický originál a plná specifikace:** [IPD na 3GPP Explorer](https://3gpp-explorer.com/glossary/ipd/)
