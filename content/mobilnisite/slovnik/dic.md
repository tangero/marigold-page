---
slug: "dic"
url: "/mobilnisite/slovnik/dic/"
type: "slovnik"
title: "DIC – Disregard Incoming Call"
date: 2025-01-01
abbr: "DIC"
fullName: "Disregard Incoming Call"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/dic/"
summary: "DIC je doplňková služba v GSM/UMTS/LTE, která umožňuje obsluhovanému uživateli dočasně odmítnout všechny příchozí hovory. Při aktivaci síť zabraňuje pokusům o sestavení hovoru k uživateli, prezentuje"
---

DIC je doplňková služba v sítích GSM/UMTS/LTE, která umožňuje uživateli dočasně odmítnout všechny příchozí hovory, čímž síť zabrání sestavení hovoru a prezentuje obsazený tón nebo přesměruje do hlasové schránky.

## Popis

Doplňková služba Disregard Incoming Call (DIC) je síťová funkce, která umožňuje účastníkovi instruovat síť, aby odmítla všechny příchozí hovory v okruhově spínané hlasové službě určené pro jeho linku. Když uživatel službu aktivuje, Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo MSC Server zachytí jakýkoli příchozí požadavek na sestavení hovoru (např. zprávu [IAM](/mobilnisite/slovnik/iam/) v [SS7](/mobilnisite/slovnik/ss7/)) určený pro tohoto účastníka. Místo dokončení hovoru síť vrátí volající straně specifickou hodnotu příčiny, typicky označující, že uživatel je obsazený nebo že hovor je odmítnut. To má za následek, že volající strana slyší obsazený tón nebo je směrována do systému hlasové schránky, pokud je k němu předplatitel přihlášen.

Architektonicky je logika služby umístěna v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) a je prováděna MSC, které uživatele obsluhuje. HLR ukládá profil služeb účastníka, včetně stavu aktivace DIC. Když uživatel DIC aktivuje nebo deaktivuje, tento stav je aktualizován v HLR. Během procedur ukončení hovoru obsluhující MSC dotazuje HLR (prostřednictvím [MAP](/mobilnisite/slovnik/map/) zpráv) nebo používá lokálně uložené informace z profilu, aby zkontrolovala, zda je DIC aktivní. Pokud je aktivní, MSC aplikuje logiku služby a hovor odmítne. Službu může uživatel vyvolat pomocí kódů Unstructured Supplementary Service Data ([USSD](/mobilnisite/slovnik/ussd/)) (např. *#43#), prostřednictvím menu v telefonu, které generuje příslušnou signalizaci, nebo prostřednictvím interaktivního hlasového systému.

Klíčovými komponentami, které jsou zapojeny, jsou UE (pro vyvolání služby), MSC/MSC Server (pro provedení služby) a HLR (pro uložení profilu služeb). Služba funguje na bázi jednotlivého uživatele a vztahuje se na všechny příchozí hlasové hovory bez ohledu na identitu volajícího. Obvykle neovlivňuje [SMS](/mobilnisite/slovnik/sms/) nebo paketově spínané datové relace. Jejím úkolem v síti je poskytnout základní, ale nezbytnou funkci správy hovorů řízenou uživatelem, která zvyšuje pohodlí a soukromí účastníka. Funguje nezávisle, ale může být doplňkem k dalším službám blokování hovorů, jako je Call Deflection nebo Call Forwarding on Busy.

## K čemu slouží

Služba DIC byla vytvořena, aby poskytla mobilním účastníkům přímou a okamžitou kontrolu nad příjmem hovorů a naplnila tak základní potřebu soukromí a nepřerušovaného času. Před rozšířením sofistikovaných smartphonů s režimy 'nerušit' byly síťové služby jako DIC primárním prostředkem, jak uživatelé mohli dočasně blokovat všechny příchozí hovory bez vypnutí telefonu nebo vyjmutí [SIM](/mobilnisite/slovnik/sim/) karty. Řešila problém nechtěných přerušení během schůzek, spánku nebo osobního času.

Historicky byla součástí sady doplňkových služeb GSM standardizovaných od raných fází (Fáze 1/2) a přenesena do domén okruhově spínané služby 3GPP UMTS a LTE. Odstraňovala omezení starších telefonních systémů, kde odmítnutí hovoru vyžadovalo manuální zásah (neodpovědět) nebo fyzické odpojení. DIC poskytuje síťově vynucenou záruku, že žádné hovory neprojdou. Motivací bylo zvýšit spokojenost účastníků a napodobit funkce pevných linek, zatímco síťovým operátorům umožnilo nabízet diferencované balíčky služeb. Je to jednodušší alternativa k podmíněnému přesměrování hovoru, protože nevyžaduje konfiguraci cílových čísel.

## Klíčové vlastnosti

- Síťové odmítnutí všech příchozích hovorů v okruhově spínané hlasové službě
- Aktivace/deaktivace pomocí USSD kódů (např. *#43#) nebo menu telefonu
- Stav uložen v profilu účastníka v HLR
- Způsobí, že síť vrátí volajícímu příčinu 'uživatel obsazen' nebo podobnou
- Neovlivňuje odchozí hovory, SMS nebo datové relace
- Poskytuje okamžitou funkci 'nerušit' bez vypnutí telefonu

## Související pojmy

- [USSD – Unstructured Supplementary Services Data](/mobilnisite/slovnik/ussd/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TS 27.002** (Rel-19) — Terminal Adaptation Functions for Asynchronous Services

---

📖 **Anglický originál a plná specifikace:** [DIC na 3GPP Explorer](https://3gpp-explorer.com/glossary/dic/)
