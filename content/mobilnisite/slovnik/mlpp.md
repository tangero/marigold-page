---
slug: "mlpp"
url: "/mobilnisite/slovnik/mlpp/"
type: "slovnik"
title: "MLPP – Multi-Level Precedence and Pre-emption"
date: 2025-01-01
abbr: "MLPP"
fullName: "Multi-Level Precedence and Pre-emption"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mlpp/"
summary: "Služba poskytující prioritní zpracování hovorů a přednostní obsazení prostředků v okruhově komutovaných sítích. Přiřazuje hovorům úrovně přednosti, což umožňuje hovorům s vysokou prioritou (např. nouz"
---

MLPP je služba v okruhově komutovaných sítích, která přiřazuje hovorům úrovně přednosti, což umožňuje hovorům s vysokou prioritou přednostně obsadit síťové prostředky nebo se zařadit před hovory s nižší prioritou, a tím zajistit kritickou komunikaci při přetížení sítě.

## Popis

Multi-Level Precedence and Pre-emption (MLPP) je telekomunikační služba navržená pro kritickou a nouzovou komunikaci. Funguje v rámci okruhově komutovaných domén, především v sítích GSM a UMTS, a řídí zřizování hovorů a přidělování prostředků na základě přiřazených úrovní priority. Základním principem je, že hovor s vyšší úrovní přednosti může přednostně obsadit (přerušit nebo zamítnout) hovor s nižší úrovní přednosti, pokud jsou síťové prostředky (jako provozní kanály nebo spojové okruhy) přetíženy. MLPP zahrnuje všechny síťové prvky na cestě hovoru, včetně mobilní stanice ([MS](/mobilnisite/slovnik/ms/)), základnové stanice ([BSS](/mobilnisite/slovnik/bss/)), ústředny mobilní sítě ([MSC](/mobilnisite/slovnik/msc/)) a případných tranzitních ústředen.

Služba funguje tak, že hovoru je v místě jeho vzniku přiřazena úroveň přednosti. Tato úroveň je zakódována v signalizaci pro zřízení hovoru (např. ve zprávě Setup). Úrovně přednosti jsou obvykle definovány hierarchicky, například od úrovně 0 (nejnižší, běžná) do úrovně 4 (nejvyšší, flash override). Když síťový uzel, jako je MSC, zpracovává požadavek na zřízení hovoru, ověřuje požadovanou úroveň přednosti vůči dostupnosti svých prostředků a úrovním přednosti probíhajících hovorů. Pokud prostředky nejsou dostupné, uzel rozhodne, zda má nový hovor vyšší přednost než kterýkoli z probíhajících hovorů využívajících požadovaný prostředek. Pokud ano, může přednostně obsadit hovor(y) s nižší prioritou, čímž uvolní prostředek pro hovor s vyšší prioritou. Přednostně obsazené straně je přehrán tón přednostního obsazení a spojení je ukončeno.

MLPP také zahrnuje funkci řazení do fronty. Pokud hovor s vysokou prioritou nemůže být kvůli přetížení okamžitě dokončen a zároveň nemůže přednostně obsadit jiný hovor, protože všechny prostředky jsou obsazeny hovory se stejnou nebo vyšší prioritou, může být zařazen do prioritní fronty. Síť tyto fronty spravuje a snaží se zařazený hovor dokončit, jakmile se uvolní vhodný prostředek. Služba vyžaduje předplatné a autorizaci; ne všem uživatelům je povoleno zahajovat hovory na nejvyšších úrovních přednosti. MLPP je hluboce integrována se signalizačními protokoly, jako je [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)), a s funkcemi řízení hovorů v rámci MSC. V systémech 3GPP její specifikace zajišťují interoperabilitu pro prioritní služby napříč administrativními doménami, což je klíčové pro telekomunikace národní bezpečnosti a připravenosti na mimořádné události ([NS/EP](/mobilnisite/slovnik/ns-ep/)).

## K čemu slouží

MLPP byla vyvinuta k uspokojení kritické potřeby garantovaných komunikačních kanálů pro vládní, vojenské a záchranné složky, zejména při přetížení sítě nebo v krizových situacích. Ve veřejných telefonních sítích ([PSTN](/mobilnisite/slovnik/pstn/)) a raných mobilních sítích byly všechny hovory v době vytížení zpracovávány se stejnou prioritou, což znamenalo, že kritický nouzový hovor mohl být zablokován stejně snadno jako běžný společenský hovor. To bylo pro národní bezpečnost, reakci na katastrofy a vojenské operace nepřijatelné.

Zavedení MLPP poskytlo standardizovaný mechanismus pro zavedení víceúrovňové prioritní hierarchie do sítě. Řeší problém soupeření o prostředky tím, že umožňuje autorizovaným hovorům s vysokou prioritou 'prořezat se' přetížením. Tím je zajištěno, že komunikace pro velení a řízení, koordinace záchranných prací a další životně důležité hovory mohou být zřízeny i při extrémním zatížení sítě, například během přírodních katastrof nebo veřejných krizových situací. Její přijetí do standardů 3GPP již od raných verzí GSM zajistilo, že mobilní sítě mohou tyto požadavky vládních a záchranných služeb podporovat, a staly se tak spolehlivou součástí národní infrastruktury.

## Klíčové vlastnosti

- Definice více hierarchických úrovní přednosti hovorů (např. Routine, Priority, Immediate, Flash, Flash Override)
- Schopnost přednostního obsazení, při kterém hovory s vyšší prioritou mohou obsadit prostředky od hovorů s nižší prioritou
- Prioritní řazení do fronty pro hovory, které nemohou být okamžitě dokončeny
- Autorizace a řízení předplatného pro zahajování hovorů s vysokou úrovní přednosti
- Kompletní signalizace úrovně přednosti napříč sítí
- Slyšitelný tón přednostního obsazení a upozornění přednostně obsazené straně

## Definující specifikace

- **TR 22.950** (Rel-19) — Feasibility Study on Priority Service
- **TS 24.067** (Rel-19) — eMLPP Supplementary Service Procedures
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks

---

📖 **Anglický originál a plná specifikace:** [MLPP na 3GPP Explorer](https://3gpp-explorer.com/glossary/mlpp/)
