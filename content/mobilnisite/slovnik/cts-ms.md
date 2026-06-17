---
slug: "cts-ms"
url: "/mobilnisite/slovnik/cts-ms/"
type: "slovnik"
title: "CTS-MS – Cordless Telephony System - Mobile Station"
date: 2025-01-01
abbr: "CTS-MS"
fullName: "Cordless Telephony System - Mobile Station"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cts-ms/"
summary: "CTS-MS je mobilní koncové zařízení v systému bezšňůrové telefonie (Cordless Telephony System) 3GPP, umožňující bezdrátové hlasové a datové služby v domácím/podnikovém prostředí. Funguje jako dvou reži"
---

CTS-MS je mobilní koncové zařízení v systému bezšňůrové telefonie (Cordless Telephony System) standardizovaném 3GPP, které funguje jako dvou režimové zařízení poskytující bezdrátové hlasové/datové služby a plynulý přechod mezi pokrytím bezšňůrové sítě v domácnosti/kanceláři a širokoplošnými celulárními sítěmi.

## Popis

Cordless Telephony System - Mobile Station (CTS-MS) je specializované mobilní koncové zařízení definované v rámci architektury systému bezšňůrové telefonie (Cordless Telephony System) 3GPP. Jako součást uživatelského vybavení (UE) slouží jako fyzické zařízení, které účastníci používají pro přístup ke službám [CTS](/mobilnisite/slovnik/cts/), fungující jako radiový koncový bod komunikující s pevnou částí systému bezšňůrové telefonie ([CTS-FP](/mobilnisite/slovnik/cts-fp/)). CTS-MS implementuje kompletní protokolový zásobník vyžadovaný pro provoz CTS, včetně přenosu na fyzické vrstvě, řízení přístupu k médiu a signalizačních protokolů vyšších vrstev specifikovaných v 3GPP TS 45.056 a souvisejících specifikacích.

Z architektonického hlediska obsahuje CTS-MS několik klíčových komponent: radiový transceiver pracující ve vyhrazených kmitočtových pásmech (typicky 1880-1900 MHz v Evropě), jednotky pro základní pásmo (baseband) pro modulaci/demodulaci, software pro zpracování protokolů, prvky uživatelského rozhraní (klávesnice, displej, mikrofon, reproduktor) a systémy pro správu napájení. Zařízení podporuje více přístup s časovým dělením (TDMA) s dynamickou alokací kanálů a implementuje specifickou rámcovou strukturu a formáty přenosových dávek definované pro CTS. Udržuje synchronizaci s CTS-FP prostřednictvím vyhrazených synchronizačních kanálů a provádí kontinuální měření kvality signálu pro podporu rozhodování o předání spojení.

Během provozu CTS-MS sleduje definovaný stavový automat s režimy idle, přístupovým a vyhrazeným. V režimu idle monitoruje volací kanály od CTS-FP a zároveň provádí výběr/převýběr buňky na základě přijímané úrovně signálu a systémových parametrů. Při zahájení nebo přijetí hovoru přechází přes procedury náhodného přístupu k založení vyhrazeného kanálu pro přenos hovoru. CTS-MS implementuje komplexní funkce správy mobility včetně registrace polohy, autentizačních procedur využívajících moduly identity účastníka (SIM) a provádění předání spojení mezi různými CTS-FP v rámci stejného systému.

CTS-MS hraje klíčovou roli v celkové architektuře CTS tím, že poskytuje radiové rozhraní koncovým uživatelům a zároveň udržuje požadavky na kompatibilitu s infrastrukturou pevné sítě. Podporuje jak hlasové služby využívající adaptivní vícerychlostní kodeky, tak základní datové služby prostřednictvím spojově orientovaných připojení. Dvou režimová schopnost zařízení (pokud je implementována) umožňuje automatický nebo manuální výběr mezi sítěmi CTS a celulárními sítěmi na základě dostupnosti pokrytí a uživatelských preferencí, s inteligencí upřednostňovat CTS při pobytu v jeho pokrytí za účelem optimalizace nákladů a potenciálně lepší kvality hovoru v indoor prostředích.

## K čemu slouží

CTS-MS byl vyvinut pro uspokojení rostoucí poptávky po dostupné, kvalitní bezdrátové telefonii v domácím a malopodnikovém prostředí. Před jeho standardizací dominovaly na trhu proprietární systémy bezšňůrových telefonů, což vedlo k problémům s interoperabilitou, omezené sadě funkcí a vázanosti na konkrétního dodavatele. Specifikace [CTS](/mobilnisite/slovnik/cts/) od 3GPP si kladla za cíl vytvořit standardizovaný systém bezšňůrové telefonie, který by mohl využít pokrok v celulární technologii a zároveň poskytovat lepší kvalitu hovoru a spolehlivější indoor pokrytí než existující analogové bezšňůrové systémy.

Tato technologie řešila několik klíčových problémů: poskytla standardizovanou alternativu k proprietárním systémům [DECT](/mobilnisite/slovnik/dect/) v regionech, kde DECT nebyl dominantní, nabídla lepší spektrální účinnost prostřednictvím digitální TDMA technologie a umožnila plynulou integraci s celulárními sítěmi prostřednictvím dvou režimových schopností. Tím se vyřešila omezení dřívějších bezšňůrových systémů, které trpěly špatnou kvalitou hovoru, omezeným dosahem, bezpečnostními zranitelnostmi vůči odposlechu a neschopností integrace s mobilními sítěmi pro širší pokrytí.

Historicky se CTS objevil jako součást snah 3GPP rozšířit technologii GSM do nových tržních segmentů mimo tradiční celulární služby. Vytvořením standardizovaného systému bezšňůrové telefonie založeného na principech GSM mohli operátoři nabízet integrované služby domácí zóny s preferenčním tarifem, zatímco výrobci mohli vyvíjet zařízení pro více trhů bez nutnosti regionálních úprav. CTS-MS konkrétně umožnil tuto vizi tím, že poskytl standardizované koncové zařízení, které mohlo pracovat jak v bezšňůrovém, tak celulárním režimu, a tím překlenul mezeru mezi pevnou a mobilní telefonií.

## Klíčové vlastnosti

- Dvou režimový provoz podporující jak sítě CTS, tak celulární sítě
- Více přístup založený na TDMA s dynamickou alokací kanálů
- Podpora adaptivních vícerychlostních hlasových kodeků
- Autentizace účastníka prostřednictvím SIM karty
- Plynulé předání spojení mezi pevnými částmi CTS
- Energeticky úsporný provoz pro delší výdrž baterie

## Související pojmy

- [CTS-FP – Cordless Telephony System - Fixed Part](/mobilnisite/slovnik/cts-fp/)
- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TS 42.056** (Rel-19) — GSM Cordless Telephony System (CTS)
- **TS 43.020** (Rel-19) — Security Procedures for GSM
- **TS 43.052** (Rel-19) — GSM Cordless Telephony System (CTS) Radio Interface
- **TS 45.056** (Rel-19) — GSM CTS-FP Radio Requirements

---

📖 **Anglický originál a plná specifikace:** [CTS-MS na 3GPP Explorer](https://3gpp-explorer.com/glossary/cts-ms/)
