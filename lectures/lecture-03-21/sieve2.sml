(* ****** ****** *)
use "./../../mysmlib/mysmlib-cls.sml";
(* ****** ****** *)

fun
sieve
(fxs: int stream): int stream = fn() =>
(
case fxs() of
  strcon_nil => strcon_nil
| strcon_cons(x1, fxs) =>
  strcon_cons(x1, sieve(filter(fxs, x1)))
)

and
filter
( fxs
: int stream, x0: int): int stream =
stream_make_filter(fxs, fn(x1) => x1 mod x0 > 0)

(* ****** ****** *)

fun
stream_from(n: int): int stream =
fn () => strcon_cons(n, stream_from(n+1))

(* ****** ****** *)

val thePrimes = sieve(stream_from(2))

(* ****** ****** *)

(* end of [CS320-2023-Spring-lectures-sieve.sml] *)