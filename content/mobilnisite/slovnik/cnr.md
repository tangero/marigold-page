---
slug: "cnr"
url: "/mobilnisite/slovnik/cnr/"
type: "slovnik"
title: "CNR – Completion of Communications on No Reply"
date: 2025-01-01
abbr: "CNR"
fullName: "Completion of Communications on No Reply"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cnr/"
summary: "CNR je doplňková služba, která automaticky dokončí hovor, když volaný účastník neodpoví v určeném čase. Přesměruje hovor na hlasovou schránku nebo jiný cíl, čímž zlepšuje míru dokončení hovorů a uživa"
---

CNR je doplňková služba, která automaticky přesměruje nezodpovězený hovor na cílové zařízení, například hlasovou schránku, po uplynutí nastaveného času, čímž zlepšuje dokončení hovoru.

## Popis

Completion of Communications on No Reply (CNR, Dokončení komunikace při neodpovědi) je standardizovaná doplňková služba v rámci specifikací 3GPP, která poskytuje automatizované mechanismy pro dokončení hovoru, když volaný účastník nezodpoví příchozí hovor. Služba funguje v architektuře IP Multimedia Subsystem (IMS) a je implementována prostřednictvím specifických procedur řízení relace definovaných ve specifikacích 3GPP. Při zahájení hovoru služba CNR monitoruje proces navázání hovoru a detekuje, když zařízení volaného účastníka zvoní, ale nedojde k odpovědi v předem stanoveném časovém intervalu, který je obvykle konfigurovatelný operátorem sítě nebo účastníkem.

Technická implementace CNR zahrnuje koordinaci více síťových prvků. Serving-Call Session Control Function (S-CSCF) hraje klíčovou roli tím, že aplikuje počáteční filtrační kritéria pro identifikaci hovorů, které mají být ošetřeny službou CNR. Při vyvolání CNR S-CSCF komunikuje s Application Server ([AS](/mobilnisite/slovnik/as/)), který hostí logiku CNR. AS určuje příslušný cílový bod přesměrování na základě preferencí účastníka a síťových politik, což může zahrnovat systémy hlasové schránky, alternativní čísla nebo služby hlasových oznámení. Služba používá rozšíření signalizace SIP pro správu procesu přesměrování hovoru při zachování správných záznamů o účtování a zajištění kontinuity služby.

Mezi klíčové architektonické komponenty patří Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), který ukládá údaje o předplatném CNR, Telephony Application Server (TAS), který implementuje servisní logiku, a Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)), která může poskytovat hlasová oznámení během přesměrování hovoru. Služba funguje ve spojení s dalšími doplňkovými službami, jako je Call Forwarding Unconditional ([CFU](/mobilnisite/slovnik/cfu/)) a Call Forwarding on Busy ([CFB](/mobilnisite/slovnik/cfb/)), ale specificky řeší scénář neodpovědi. Implementace CNR vyžaduje pečlivou koordinaci časování, aby bylo možné rozlišit mezi skutečnými situacemi neodpovědi a případy, kdy volaný účastník potřebuje k odpovědi více času.

Služba podporuje jak scénáře iniciující (originating), tak koncové (terminating), což znamená, že může být aplikována na základě předplatného volajícího účastníka (originating CNR) nebo volaného účastníka (terminating CNR). Síťoví operátoři mohou konfigurovat různé hodnoty časového limitu pro různé kategorie účastníků a implementovat obchodní pravidla pro případy, kdy má být CNR vyvoláno. Služba také zahrnuje ustanovení pro zpracování scénářů mezinárodního roamingu, což zajišťuje konzistentní chování bez ohledu na polohu účastníka. Správná implementace vyžaduje integraci se systémy účtování, aby bylo zajištěno přesné fakturování přesměrovaných hovorů a kompatibilita s požadavky na zákonné odposlechy.

## K čemu slouží

CNR bylo vyvinuto k řešení významného problému neúspěšného dokončení hovorů způsobeného nezodpovězenými hovory, které představovaly podstatnou část neúspěšných pokusů o hovor v mobilních sítích. Před standardizovanou implementací CNR používali síťoví operátoři proprietární řešení pro služby dokončení hovorů, což vedlo k problémům s interoperabilitou, zejména v roamingových scénářích a mezi sítěmi různých operátorů. Nedostatek standardizace znamenal nekonzistentní uživatelský zážitek, složité mezifiremní dohody a obtíže při implementaci pokročilých funkcí přes síťové hranice.

Služba řeší několik praktických problémů v telekomunikačních sítích. Za prvé zlepšuje celkovou efektivitu sítě snížením doby, po kterou jsou síťové zdroje vázány čekáním na přirozené vypršení časového limitu u nezodpovězených hovorů. Za druhé zlepšuje uživatelský zážitek poskytováním předvídatelného a konzistentního chování pro nezodpovězené hovory napříč různými sítěmi a zařízeními. Za třetí umožňuje operátorům příjmové příležitosti prostřednictvím služeb hlasové schránky a alternativních možností dokončení hovoru. Standardizace v 3GPP Release 8 umožnila harmonizovanou implementaci napříč sítěmi LTE a IMS, což usnadnilo globální interoperabilitu.

Historicky podobná funkčnost existovala v okruhově přepínaných sítích prostřednictvím různých proprietárních implementací, ale migrace na IP sítě vyžadovala nový přístup. CNR v kontextu IMS muselo fungovat se signalizací SIP, podporovat multimediální relace přesahující hlas a integrovat se s dalšími službami IMS. Standardizace 3GPP zajistila, že CNR bude bezproblémově fungovat s dalšími doplňkovými službami a podporovat vyvíjející se požadavky moderní telekomunikace, včetně podpory videohovorů a multimediálního zasílání zpráv v pozdějších vydáních.

## Klíčové vlastnosti

- Automatické přesměrování hovoru po konfigurovatelném časovém limitu neodpovědi
- Integrace s architekturou IMS využívající signalizaci SIP
- Podpora jak iniciujících (originating), tak koncových (terminating) servisních scénářů
- Konfigurovatelné cíle přesměrování včetně hlasové schránky a alternativních čísel
- Podpora roamingu s konzistentním chováním napříč navštívenými sítěmi
- Kompatibilita s dalšími doplňkovými službami a funkcemi zákazu hovorů

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 24.447** (Rel-8) — Advice Of Charge (AOC) Service Protocol
- **TS 24.642** (Rel-19) — CCBS/CCNR/CCNL SIP Protocol Specification
- **TS 24.647** (Rel-19) — Advice of Charge (AOC) service protocol

---

📖 **Anglický originál a plná specifikace:** [CNR na 3GPP Explorer](https://3gpp-explorer.com/glossary/cnr/)
