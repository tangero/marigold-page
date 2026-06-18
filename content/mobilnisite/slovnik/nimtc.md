---
slug: "nimtc"
url: "/mobilnisite/slovnik/nimtc/"
type: "slovnik"
title: "NIMTC – Network Improvements for Machine Type Communications"
date: 2025-01-01
abbr: "NIMTC"
fullName: "Network Improvements for Machine Type Communications"
category: "IoT"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nimtc/"
summary: "Pracovní položka 3GPP a soubor funkcí zaměřených na vylepšení buněčných sítí pro efektivní podporu obrovského počtu nízkonákladových a nízkopříkonových zařízení pro Machine Type Communication (MTC). Ř"
---

NIMTC je pracovní položka 3GPP zahrnující funkce, které vylepšují buněčné sítě tak, aby efektivně podporovaly obrovský počet nízkonákladových a nízkopříkonových zařízení pro MTC, a to řešením přetížení jádra sítě, zahlcení signalizací a spotřeby energie.

## Popis

Network Improvements for Machine Type Communications (NIMTC, síťová vylepšení pro komunikaci mezi stroji) označuje komplexní soubor architektonických vylepšení, protokolů a funkcí standardizovaných 3GPP pro přizpůsobení mobilních sítí jedinečným požadavkům komunikace mezi stroji ([MTC](/mobilnisite/slovnik/mtc/)). Na rozdíl od lidsky orientovaného mobilního širokopásmového připojení zahrnuje MTC komunikaci mezi stroji (senzory, akční členy, měřiče) nebo ze strojů na servery, pro kterou je charakteristický přenos malých, málo frekventovaných dat, obrovský počet zařízení a požadavky na ultra nízkou spotřebu energie a nízké náklady. Práce na NIMTC se týká jak rádiové přístupové sítě, tak jádra sítě a servisní vrstvy, s cílem zmírnit síťové přetížení a umožnit škálovatelná nasazení IoT.

Klíčové architektonické komponenty zavedené nebo vylepšené v rámci NIMTC zahrnují Machine-Type Communication Interworking Function ([MTC-IWF](/mobilnisite/slovnik/mtc-iwf/)) a Service Capability Exposure Function ([SCEF](/mobilnisite/slovnik/scef/)). MTC-IWF, zavedená dříve, funguje jako brána mezi jádrem sítě a externími servery MTC a zajišťuje spouštění zařízení prostřednictvím [SMS](/mobilnisite/slovnik/sms/) nebo metodami řídicí roviny. SCEF, pokročilejší entita zavedená později, poskytuje standardizované [API](/mobilnisite/slovnik/api/) pro bezpečné zpřístupnění služeb a umožňuje funkce jako Non-IP Data Delivery ([NIDD](/mobilnisite/slovnik/nidd/)) nebo odběr síťových událostí. NIMTC také vedlo k definici nových kategorií zařízení, jako jsou Cat-0, Cat-M1 a NB-IoT, které jsou optimalizované pro nízký příkon a rozšířené pokrytí.

Vylepšení působí na více vrstvách. Na rádiové straně NIMTC zahrnuje funkce jako Extended Discontinuous Reception (eDRX) a Power Saving Mode ([PSM](/mobilnisite/slovnik/psm/)), které umožňují zařízením spát po delší dobu a dramaticky tak snižují spotřebu baterie. Optimalizace signalizace je dosaženo řešeními jako Overload Control for MTC, které zabraňuje kolapsu sítě při hromadné aktivaci zařízení (např. po výpadku proudu), a využitím optimalizací řídicí roviny (jako je NIDD) k vyhnutí se vytváření datových přenosových kanálů pro malé pakety. Vylepšení jádra sítě zahrnují úpravy procedur správy mobility a správy relací tak, aby byly lehčí a efektivnější pro zařízení, která jsou stacionární nebo mají předvídatelné vzorce mobility.

Úlohou NIMTC je transformovat síť navrženou pro kontinuální, vysokorychlostní komunikaci na síť schopnou efektivně obsluhovat miliardy sporadicky připojených koncových bodů s nízkou přenosovou rychlostí. Zahrnuje holistický pohled a řeší potenciální úzká místa od rádiového modemu zařízení až po aplikační server. Tato práce zajišťuje, že provoz MTC nezhoršuje výkon tradičních služeb mobilního širokopásmového připojení, a zároveň umožňuje nové vertikální trhy, jako jsou utility, zemědělství a chytrá města.

## K čemu slouží

NIMTC bylo zahájeno, protože tradiční sítě 3GPP nebyly vhodné pro očekávanou explozi zařízení [MTC](/mobilnisite/slovnik/mtc/). Sítě byly optimalizovány pro lidský provoz: relativně málo zařízení generujících kontinuální, objemné datové relace s častou mobilitou. MTC představovalo opačný profil: obrovský počet zařízení posílajících malé pakety nepravidelně, často z pevných lokalit. Tento nesoulad způsobil několik kritických problémů: jádro sítě mohlo být zaplaveno signalizačními bouřemi způsobenými současnými požadavky na připojení od milionů zařízení; spotřeba energie rádiových modulů vždy připravených naslouchat byla neúnosná pro bateriová zařízení určená k provozu po mnoho let; a náklady a složitost plných IP zásobníků na jednoduchých senzorech byly příliš vysoké.

Primárním cílem bylo umožnit 'massive MTC' (mMTC) jako jeden ze tří pilířů 5G (společně s enhanced mobile broadband a ultra-reliable low latency communications). Bez NIMTC by škálování na desítky miliard zařízení IoT bylo ekonomicky a technicky nemožné kvůli síťovému přetížení a ceně zařízení. Řešilo to omezení sítí před 3GPP Release 10, které zacházely s každým připojeným zařízením, ať už šlo o smartphone nebo senzor, stejnými náročnými procedurami.

Historicky práce na NIMTC začaly v 3GPP Release 10, zpočátku se zaměřovaly na řízení přetížení jádra sítě a spouštění zařízení. Následující verze rozšířily záběr na optimalizace rádiového přístupu (vedoucí k LTE-M a NB-IoT), funkce pro úsporu energie a architektonické prvky jako SCEF. Tento vývoj odráží posun od pouhého zabránění selhání sítě při zatížení MTC k aktivnímu vytváření efektivní, službami vybavené platformy pro IoT, která položila základy pro optimalizace Cellular IoT (CIoT) plně realizované ve verzích 13 a novějších.

## Klíčové vlastnosti

- Mechanismy pro řízení přetížení a zahlcení signalizace MTC (např. ACB, EAB)
- Power Saving Mode (PSM) a extended Discontinuous Reception (eDRX) pro prodloužení životnosti baterie
- Zavedení kategorií zařízení s nízkou složitostí (Cat-0, Cat-M1, NB-IoT)
- Optimalizace CIoT EPS/5GS v řídicí rovině (včetně NIDD)
- Service Capability Exposure Function (SCEF/NEF) pro zpřístupnění síťového API
- Rozšířené metody spouštění zařízení nad rámec SMS (prostřednictvím řídicí roviny)

## Související pojmy

- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)
- [MTC-IWF – Machine Type Communications - InterWorking Function](/mobilnisite/slovnik/mtc-iwf/)
- [PSM – Protocol State Machine](/mobilnisite/slovnik/psm/)

## Definující specifikace

- **TS 22.368** (Rel-19) — Network Improvements for Machine Type Communications
- **TR 22.988** (Rel-19) — Study on MTC Numbering Alternatives

---

📖 **Anglický originál a plná specifikace:** [NIMTC na 3GPP Explorer](https://3gpp-explorer.com/glossary/nimtc/)
