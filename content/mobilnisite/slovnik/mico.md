---
slug: "mico"
url: "/mobilnisite/slovnik/mico/"
type: "slovnik"
title: "MICO – Mobile Initiated Connection Only"
date: 2026-01-01
abbr: "MICO"
fullName: "Mobile Initiated Connection Only"
category: "IoT"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mico/"
summary: "Režim úspory energie UE pro zařízení IoT, ve kterém síť zařízení nestránkuje. Zařízení se stane dosažitelným pro služby iniciované sítí (mobile-terminated) pouze při vlastní iniciaci komunikace, což v"
---

MICO je režim úspory energie UE pro zařízení IoT, ve kterém síť nemůže stránkovat zařízení, takže se stane dosažitelným pro služby iniciované sítí (mobile-terminated) pouze tehdy, když samo zahájí komunikaci.

## Popis

Mobile Initiated Connection Only (MICO) je funkce pro úsporu energie definovaná ve standardech 3GPP, primárně pro IoT a další zařízení s omezenou kapacitou baterie. Zásadně mění tradiční model dosažitelnosti. Ve standardním připojení 3GPP může síť stránkovat UE kdykoli během jejího registrovaného stavu, aby doručila data nebo signalizaci iniciovanou sítí, což vyžaduje, aby UE periodicky naslouchala stránkovacím zprávám. Režim MICO tuto možnost stránkování ze strany sítě deaktivuje. Když se UE registruje v síti a indikuje podporu MICO, síť jí přidělí MICO-specifickou Allowed [NSSAI](/mobilnisite/slovnik/nssai/) a podle toho nakonfiguruje funkci Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)). Po úspěšné registraci UE přejde do stavu hlubokého spánku. AMF odmítne všechny požadavky iniciované sítí (například zprávy Session Management nebo Data Notification ze [SMF](/mobilnisite/slovnik/smf/)/[UPF](/mobilnisite/slovnik/upf/)) s příčinou (cause) indikující, že UE není dosažitelná. Síť může na základě politiky tyto downlink data bufferovat nebo zahodit. Dosažitelnost je obnovena pouze tehdy, když UE sama iniciuje proceduru Service Request, typicky spuštěnou vlastními uplink daty nebo vypršením periodického časovače Registration Update. Tato procedura převede UE do připojeného stavu (connected state), což umožní doručení jakýchkoli buffrovaných downlink dat. Stav řízení rádiových prostředků (Radio Resource Control - [RRC](/mobilnisite/slovnik/rrc/)) UE v režimu MICO je typicky RRC_IDLE, ale s klíčovým rozdílem, že nesleduje stránkovací kanál, což vede k podstatné úspoře energie. Funkce je vyjednána během registrační procedury prostřednictvím indikace MICO v Registration Request od UE a indikace MICO sítě v Registration Accept. Síťové parametry, jako je Active Time a Periodic Registration Timer, jsou také nakonfigurovány pro řízení spánkových cyklů UE a povinných kontrolních kontaktů.

## K čemu slouží

MICO bylo vytvořeno, aby řešilo kritickou výzvu životnosti baterie pro zařízení hromadné komunikace strojového typu (massive Machine-Type Communication - mMTC) v 5G a dalších generacích. Tradiční mobilní zařízení, i v režimu nečinnosti (idle mode), se musí často probouzet, aby naslouchala stránkovacím zprávám, což v čase spotřebovává významnou energii. Pro IoT senzory, měřiče nebo trackery, které posílají data nepravidelně (např. jednou denně), ale mají pracovat roky na jedné baterii, je tato neustálá připravenost na downlink provoz plýtvavá a nepraktická. MICO to řeší přechodem na čistě model komunikace iniciované zařízením (mobile-originated), čímž sladí chování sítě s typickým provozním profilem mnoha IoT aplikací. Motivací byla potřeba učinit 5G sítě životaschopnými pro nasazení IoT s ultra-nízkou spotřebou a širokou oblastí pokrytí, aby konkurovaly a překonaly energetickou účinnost necelaulárních LPWAN technologií, jako jsou LoRaWAN nebo Sigfox. Eliminací odběru energie spojeného s příjmem stránkování umožňuje MICO životnost baterie v řádu desetiletí, což je klíčový požadavek pro mnoho průmyslových a smart city případů užití IoT. Představuje posun paradigmatu od 'vždy dosažitelné' k 'dosažitelné podle podmínek zařízení', optimalizující síť pro asymetrický provoz spouštěný zařízením.

## Klíčové vlastnosti

- Deaktivuje stránkování iniciované sítí (network-initiated paging) pro UE
- Vyjednáno během registrační procedury prostřednictvím NAS signalizace
- UE je dosažitelná pouze při vlastní iniciaci procedury Service Request
- AMF odmítá relace iniciované sítí (mobile-terminated sessions) s explicitní příčinou (cause) 'UE nedosažitelná'
- Podporuje rozšířené cykly nespojitého příjmu (extended discontinuous reception - eDRX) pro další úsporu energie
- Síť může aplikovat specifické politiky pro zacházení s buffrovanými downlink daty

## Související pojmy

- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 29.503** (Rel-19) — UDM Service Based Interface Stage 3
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 32.256** (Rel-19) — 5G Connection & Mobility Charging Spec
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures

---

📖 **Anglický originál a plná specifikace:** [MICO na 3GPP Explorer](https://3gpp-explorer.com/glossary/mico/)
