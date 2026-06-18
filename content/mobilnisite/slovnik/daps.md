---
slug: "daps"
url: "/mobilnisite/slovnik/daps/"
type: "slovnik"
title: "DAPS – Dual Active Protocol Stacks"
date: 2026-01-01
abbr: "DAPS"
fullName: "Dual Active Protocol Stacks"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/daps/"
summary: "Dual Active Protocol Stacks (DAPS) je vylepšení předávání spojení v 5G, které během předávání udržuje dva simultánní protokolové zásobníky – jeden pro zdrojovou buňku a jeden pro cílovou buňku. To umo"
---

DAPS je vylepšení předávání spojení v 5G, které udržuje dva simultánní protokolové zásobníky, aby umožnilo přenos dat bez přerušení a eliminovalo ztrátu paketů pro služby jako URLLC.

## Popis

Dual Active Protocol Stacks (DAPS) je sofistikovaný mechanismus předávání spojení zavedený v 5G pro dosažení připojení typu make-before-break (navázat před přerušením). Na rozdíl od tradičního předávání, kde uživatelské zařízení (UE) ukončí spojení se zdrojovou buňkou před navázáním spojení s cílovou buňkou (break-before-make), DAPS umožňuje UE udržovat dva plně aktivní a nezávislé protokolové zásobníky současně. To zahrnuje duplicitní entity Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)), Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)) a Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) pro zdrojovou a cílovou buňku. Jádrová síť zřídí tzv. split bearer (dělený nosič), kde mohou být downlinková data duplikována a odeslána jak do zdrojového, tak do cílového gNB. UE přijímá tato data z obou buněk a využívá mechanismy jako duplikace PDCP k zajištění, že alespoň jedna kopie je úspěšně doručena, čímž se eliminuje ztráta paketů během fáze provedení předání.

Z architektonického hlediska DAPS zahrnuje koordinaci mezi zdrojovým gNB, cílovým gNB a User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v jádrové síti. Zdrojový gNB zahájí přípravu předávání signalizací cílovému gNB a jádrové síti za účelem vytvoření dočasné cesty podobné dual connectivity. UPF je instruována, aby duplikovala downlinkové pakety a přeposílala je do obou gNB. Na straně UE je protokolový zásobník pro cílovou buňku zřízen a aktivován, zatímco zásobník pro zdrojovou buňku zůstává plně funkční. UE nadále vysílá uplinková data výhradně do zdrojové buňky, dokud neobdrží specifický příkaz ke switche, čímž je zajištěna kontinuita a pořadí uplinku. Toto okno s duálním příjmem přetrvává až do finálního dokončení předání, kdy je zdrojový protokolový zásobník uvolněn.

Klíčovým operačním principem je oddělení příjmu dat od příkazu k provedení předání. UE může přijímat downlinková data z cílové buňky ještě předtím, než této buňce odešle potvrzovací zprávu o předání (např. RRCReconfigurationComplete). To je zásadní posun oproti starším procedurám. Pro uplink vysílá UE data a řídicí zprávy do zdrojové buňky, dokud neobdrží explicitní indikaci '[UL](/mobilnisite/slovnik/ul/) Switch' v rámci zprávy [RRC](/mobilnisite/slovnik/rrc/) rekonfigurace, poté přepne uplinkový přenos na cílovou buňku. Tento řízený přechod zajišťuje, že nejsou ztraceny žádné uplinkové pakety. Předání DAPS je řízeno pomocí rozšířené signalizace RRC (např. v NR) a procedur Xn-AP mezi gNB, s podporou na rozhraní [NG](/mobilnisite/slovnik/ng/) pro koordinaci s jádrovou sítí.

DAPS hraje klíčovou roli v 5G rádiové přístupové síti tím, že poskytuje základ pro ultra-spolehlivou mobilitu. Jeho primární rolí je garantovat kontinuitu služeb pro náročné aplikace, jako je průmyslová automatizace, autonomní vozidla a řízení v reálném čase, kde může být i milisekundové přerušení nebo jediný ztracený paket katastrofický. Tím, že činí proceduru předávání spojení pro aplikační vrstvu prakticky neviditelnou, je DAPS klíčovým enablerem pro 5G vizi podpory komunikací pro kritické mise a splnění přísných požadavků kategorií služeb [URLLC](/mobilnisite/slovnik/urllc/).

## K čemu slouží

DAPS byl vytvořen, aby vyřešil zásadní problém přerušení dat a ztráty paketů během předávání spojení v celulárních sítích. Tradiční předávání v LTE a raném 5G následuje princip break-before-make, kde je rádiové spojení se zdrojovou buňkou přerušeno dříve, než je nové spojení s cílovou buňkou plně zajištěno. To vede k době přerušení při předání, typicky v řádu desítek až stovek milisekund, během které nelze data přenášet ani přijímat. Toto přerušení spolu s potenciální ztrátou paketů způsobenou zpožděním nebo selháním přeposílání je nepřijatelné pro nové případy užití 5G, jako je automatizace továren, telechirurgie a komunikace vozidlo-se-vším (V2X), které vyžadují 99,9999% spolehlivost a latenci pod 10 ms.

Historický kontext vychází z omezení stávajících vylepšení, jako je reportování stavu Packet Data Convergence Protocol (PDCP) a přeposílání dat mezi základnovými stanicemi, která zmírňují, ale neeliminují ztrátu paketů a špičky latence. Techniky jako podmíněné předávání zlepšují spolehlivost, ale neřeší jádrový problém doby přerušení. DAPS byl motivován potřebou radikální architektonické změny v proceduře předávání spojení pro podporu Ultra-Reliable Low-Latency Communication (URLLC), což je základní kámen 5G fáze 2 (Release 16 a novější). Přímo řeší omezení spočívající v tom, že během událostí mobility je aktivní pouze jeden protokolový zásobník rádiového spoje v daný okamžik.

Umožněním paradigmatu make-before-break DAPS tyto problémy řeší tím, že umožňuje UE připravit a aktivovat spojení s cílovou buňkou při zachování aktivního spojení se zdrojovou buňkou. To zajišťuje, že tok dat nikdy není zastaven. Účelem je tedy poskytnout předávání spojení s opravdu nulovým milisekundovým přerušením, eliminovat ztrátu paketů a drasticky snížit dopad mobility na latenci, čímž se odemkne plný potenciál 5G pro průmyslové a kritické IoT aplikace.

## Klíčové vlastnosti

- Současný provoz dvou protokolových zásobníků v UE pro zdrojovou a cílovou buňku
- Provedení předávání typu make-before-break pro nulovou dobu přerušení
- Duplikace downlinkových paketů z jádrové sítě do zdrojového i cílového gNB
- Řízený přechod uplinku ze zdrojové na cílovou buňku pomocí signalizace RRC
- Eliminace ztráty paketů během fáze provedení předání
- Podpora plynulé mobility pro služby URLLC a služby citlivé na čas

## Související pojmy

- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)

## Definující specifikace

- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 28.104** (Rel-19) — Management Data Analytics (MDA)
- **TS 28.313** (Rel-20) — Management and orchestration; SON for 5G networks
- **TS 28.541** (Rel-20) — 5G Network Resource Model (NRM) Stage 2/3
- **TS 28.552** (Rel-20) — 5G Performance Management Measurements
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.323** (Rel-19) — PDCP Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TS 36.423** (Rel-19) — X2 Application Protocol (X2AP) Specification
- **TS 37.320** (Rel-19) — Minimization of Drive Tests (MDT) Overview
- **TS 37.340** (Rel-19) — Multi-Connectivity Operation Overview
- … a dalších 13 specifikací

---

📖 **Anglický originál a plná specifikace:** [DAPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/daps/)
